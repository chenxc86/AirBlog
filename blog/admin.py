# -*- coding:utf8 -*-
"""
Author: Chenxc
Date: 2015/01/18
"""
from django.contrib import admin
from blog.models import Article, Category, Tag, ArticleImages


class ArticleImagesAdmin(admin.StackedInline):
    model = ArticleImages
    admin.site.register(ArticleImages)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tag',)
    raw_id_fields = ('author',)

    inlines = [ArticleImagesAdmin, ]

    actions = ['del_article_and_img']

    def del_article_and_img(self, request, queryset):
        for article in queryset:
            article.delete()
    del_article_and_img.short_description = u'删除文章并删除文件系统上相关图片文件'


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
