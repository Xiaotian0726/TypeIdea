"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from .custom_site import custom_site
from blog.views import post_list, post_detail, PostDetailView, IndexView, CategoryView, TagView
from config.views import links

urlpatterns = [
    # url(r'^$', post_list, name='index'),
    # url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),
    # url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),
    # url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<pk>\d+).html$', PostDetailView.as_view(), name='post-detail'),

    url(r'^links/$', links, name='links'),

    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin'),
]
