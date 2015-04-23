# -*- coding:utf8 -*-
"""
Author: Chenxc
Date: 2015/01/18
"""
from django.http import Http404
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Category, Tag, Article
from blog.forms import SearchForm
from django.db.models import Q


class GlobalContextMixin(object):
    """获取博客全局上下文数据
    """
    def get_global_context_data(self):
        global_context_data = dict()
        global_context_data['categories'] = Category.objects.all()
        global_context_data['latest'] = Article.objects.filter(status='0')[:5]

        return global_context_data


class ArticleListMixin(object):
    """重构了ListView中的get_queryset()
    """
    queryset_filter = False
    filter_model = None

    def get_queryset(self):
        if self.queryset_filter:
            condition_id = self.kwargs.get("condition_id")
            try:
                self.condition = self.filter_model.objects.get(id=condition_id)
            except self.filter_model.DoesNotExist:
                raise Http404
            self.queryset = self.condition.article_set.all()
        return super(ArticleListMixin, self).get_queryset()


class ArticleListView(GlobalContextMixin, ArticleListMixin, ListView):
    """所有文章列表（博客首页）
    """
    model = Article
    context_object_name = "articles"
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        global_context_data = self.get_global_context_data()
        if kwargs:
            global_context_data.update(**kwargs)
        return super(ArticleListView, self).get_context_data(**global_context_data)


class Search(ArticleListView):
    """站内搜索（条件：关键字）
    """
    def get_queryset(self):
        search_form = SearchForm(self.request.GET)
        if not search_form.is_valid():
            self.form_errors = search_form.errors
        else:
            query = search_form.cleaned_data
            qset = (Q(title__icontains=query["query"])|Q(content__icontains=query["query"]))
            self.queryset = Article.objects.only("status").filter(qset, status="0")
            if self.queryset:
                self.form_errors = {"query": u'以下是包含搜索关键字"%s"的本站资源' %query["query"]}
            else:
                self.form_errors = {"query": u'本站资源未包含搜索关键字"%s"' %query["query"]}
        return super(Search, self).get_queryset()
                
    def get_context_data(self, **kwargs):
        if hasattr(self, "form_errors"):
            kwargs = self.form_errors
        return super(Search, self).get_context_data(**kwargs)


class FilterCategoryView(ArticleListView):
    """按过滤条件获取相应文章列表（条件：分类）
    """
    queryset_filter = True
    filter_model = Category


class FilterTagView(ArticleListView):
    """按过滤条件获取相应文章列表（条件：标签）
    """
    queryset_filter = True
    filter_model = Tag


class ArticleDetailView(GlobalContextMixin, DetailView):
    """博客文章详情视图
    """
    model = Article
    context_object_name = "article"
    template_name = "article_detail.html"

    def get_context_data(self, **kwargs):
        global_context_data = self.get_global_context_data()
        if kwargs:
            global_context_data.update(**kwargs)
        return super(ArticleDetailView, self).get_context_data(**global_context_data)

    def get_object(self):
        object = super(ArticleDetailView, self).get_object()
        if object.status == '1':
            raise Http404
        object.heat += 1
        object.save()
        return object


class AboutView(TemplateView):
    """关于页面视图
    """
    template_name = "about.html"
