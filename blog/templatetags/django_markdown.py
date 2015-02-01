# -*- coding:utf8 -*-
"""
Author: Chenxc
Date: 2015/01/27
"""
import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='to_markdown', is_safe=True)
@stringfilter # 限定value的值为字符串
def to_markdown(value, codestyle):
    return mark_safe(markdown.markdown(value, [codestyle]))
