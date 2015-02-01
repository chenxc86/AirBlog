# -*- coding:utf8 -*-
"""
"""
from django import forms


class SearchForm(forms.Form):
    """站内搜索表单类
    """
    query = forms.CharField()
