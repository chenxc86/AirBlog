# -*- coding: utf-8 -*-
from django import template
from django.conf import settings
from django.template import Library, Node

DUOSHUO_SHORT_NAME = getattr(settings, "DUOSHUO_SHORT_NAME", None)
DUOSHUO_SECRET = getattr(settings, "DUOSHUO_SECRET", None)

register = Library()

class DuoshuoCommentsNode(Node):
    def __init__(self, short_name=DUOSHUO_SHORT_NAME, data_thread_key, data_title):
        self.short_name = short_name
        self.data_thread_key = template.Variable(data_thread_key) # 由于官方未及时对此项目进行维护，使用时报错，自行添加
                                                                  # data-thread-key 参数
        self.data_title = template.Variable(data_title) # 由于官方未及时对此项目进行维护，使用时报错，自行添加
                                                        # data-title 参数
        
    def render(self, context):
        data_thread_key = self.data_thread_key.resolve(context)
        data_title = self.data_title.resolve(context)
    
        code = '''<!-- Duoshuo Comment BEGIN -->
        <div class="ds-thread" data-thread-key="%(data_thread_key)s" data-title="%(data_title)s"></div>
        <script type="text/javascript">
        var duoshuoQuery = {short_name:"%(short_name)s"};
        (function() {
            var ds = document.createElement('script');
            ds.type = 'text/javascript';ds.async = true;
            ds.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') + '//static.duoshuo.com/embed.js';
            ds.charset = 'UTF-8';
            (document.getElementsByTagName('head')[0] 
             || document.getElementsByTagName('body')[0]).appendChild(ds);
        })();
        </script>
        <!-- Duoshuo Comment END -->''' % {"data_thread_key": data_thread_key, "short_name": self.short_name,
                                          "data_title": data_title}
        return code
    
# def duoshuo_comments(parser, token):
#     short_name = token.contents.split()   
#     if DUOSHUO_SHORT_NAME:
#         return DuoshuoCommentsNode(DUOSHUO_SHORT_NAME)
#     elif len(short_name) == 2:
#         return DuoshuoCommentsNode(short_name[1])
#     else:
#         raise template.TemplateSyntaxError, "duoshuo_comments tag takes SHORT_NAME as exactly one argument"

# 以下重写上面的 duoshuo_comments
def duoshuo_comments(parser, token):
    try:
        tag_name, data_thread_key, data_title = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    
    if DUOSHUO_SHORT_NAME:
        return DuoshuoCommentsNode(DUOSHUO_SHORT_NAME, data_thread_key, data_title)
    else:
        raise template.TemplateSyntaxError, "duoshuo_comments tag takes SHORT_NAME as exactly one argument" 

duoshuo_comments = register.tag(duoshuo_comments)

# 生成remote_auth，使用JWT后弃用
# @register.filter
# def remote_auth(value):
#     user = value
#     duoshuo_query = ds_remote_auth(user.id, user.username, user.email)
#     code = '''
#     <script>
#     duoshuoQuery['remote_auth'] = '%s';
#     </script>
#     ''' % duoshuo_query
#     return code
# remote_auth.is_safe = True
