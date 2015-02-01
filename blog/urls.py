# -*- coding:utf8 -*-
from django.conf.urls import patterns, url
from blog.views import ArticleListView, FilterCategoryView,\
                       Search, FilterTagView, ArticleDetailView, AboutView


urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^search/', Search.as_view(), name='search'),
    url(r'^filter/category/(?P<condition_id>\d+)/$', FilterCategoryView.as_view(), name='filter_category'),
    url(r'^filter/tag/(?P<condition_id>\d+)/$', FilterTagView.as_view(), name='filter_tag'),
    url(r'^article/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^about/$', AboutView.as_view(), name="about"),
)
