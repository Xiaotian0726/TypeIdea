from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag
from .adminforms import PostAdminForm

from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

# Register your models here.


# class PostInline(admin.TabularInline):
#     fields = ('title', 'desc')
#     extra = 1  # 控制额外多几个
#     model = Post


@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [PostInline, ]

    list_display = ('name', 'status', 'is_nav', 'owner', 'created_time', 'post_count')  # list_display 是展示页面展示的字段
    fields = ('name', 'status', 'is_nav')  # fields 是编辑页面需要填写的字段

    def post_count(self, obj):
        print(type(obj))
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '文章分类过滤器'
    parameter_name = 'owner_category'  # 对应的 URL 中的参数名，即 ?owner_category=X

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm

    list_display = [
        'title', 'category', 'status', 'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    list_filter = [CategoryOwnerFilter]

    # 按关键字搜索文章时，会搜索每一篇文章的以下内容
    # 使用双下划线可以加入其他 model 的属性作为搜索域
    search_fields = ['title', 'desc', 'content', 'category__name', 'tag__name']

    actions_on_top = True
    actions_on_bottom = True

    # 编辑页面
    save_on_top = True
    exclude = ['owner']
    fieldsets = (
        ('基础信息', {
            'fields': (
                ('title', 'category'),
                'status',
            )
        }),
        ('具体内容', {
            'fields': (
                'desc',
                'content',
            )
        }),
        ('额外信息', {
            'classes': ('collapse', ),
            'fields': ('tag',),
        })
    )

    filter_horizontal = ('tag', )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('custom_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def get_media(self):
        media = super().get_media()
        media.add_js(['https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js'])
        media.add_css({
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css", ),
        })
        return media


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
