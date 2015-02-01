# -*- coding:utf8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover() # 后添加，非默认配置

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Airblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
)
