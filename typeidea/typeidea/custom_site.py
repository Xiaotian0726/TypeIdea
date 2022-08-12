from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'TypeIdea'
    site_title = 'TypeIdea 后台管理'
    index_title = '首页'


custom_site = CustomSite(name='custom_admin')
