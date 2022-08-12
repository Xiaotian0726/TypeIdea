from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    exclude = ('owner', )

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        query_set = super(BaseOwnerAdmin, self).get_queryset(request)
        return query_set.filter(owner=request.user)
