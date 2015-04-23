# Airblog
博客地址: [http://www.iloveairblog.com](http://www.iloveairblog.com)

> 注意：github源码为开发版，下载源码后根据实际情况更改setting.py即可在python manage.py runserver开发服务器器下运行。

## 概述
  Airblog 是一个基于 Django 开发的博客系统，项目初衷是构建一套满足基本功能的博客系统，做到“极简”为目标，让使用者尽情书写回归博客本质，重拾文字的力量。同时也是作者对 Django 学习的一次实践，在这里与大家分享。
  
  名称的由来有些小山寨，因为项目“极简”的核心思想，所以联想到MACBOOKAIR的命名，AIR正是代表了了产品的轻薄、简单，于是Airblog诞生了。

## 目前实现功能
+ 基于Django admin的文章管理（增删改查）可 Markdown 编辑
+ 文章配图上传自动为页面引用生成缩略图
+ 按分类、标签过滤文章列表
+ 简单的站内资源搜索
+ 文章评论

## 技术实现
服务器端使用 : Python2.7 + Django1.7.3

前端展示使用 : bootstrap3

项目中集成第三方应用包括 :
+ django-pagination Django分页应用([项目主页](https://github.com/ericflo/django-pagination/))
+ duoshuo 评论系统应用([官方主页](http://duoshuo.com/))
+ grappelli 用于美化django admin样式和功能扩展

项目中需要的 Python 扩展库支持包括 :
+ pyzt 用于 Django 时区处理
+ Pillow 用于上传图片处理
+ MySQLdb 用于 Mysql 数据库操作
+ Pygments 用于代码高亮
+ Markdown2 用于markdown解析

## 项目截图
### 文章列表页截图
![文章列表页截图](https://github.com/chenxc86/Airblog/raw/master/static/img/文章列表页截图.png)
### 文章内容显示页截图
![文章列表页截图](https://github.com/chenxc86/Airblog/raw/master/static/img/文章详情页截图.png)

## 2015-02-21 修正多说插件BUG
+ 修改 duoshuo/templatetags/duoshuo_tags.py，增加两必要参数data-thread-key和data-title
+ 在文章详情页面中传入文章id和文章标题分别作为data-thread-key和data-title

多说官方建议定义data-thread-key和data-title参数用于绑定评论至相应文章，但提供的Django插件中并未提供上述参数，所以有了这次修改。

## 2015-03-08 修正文章阅读量更新影响文章内容更新时间问题
    :::python
    file name: blog/models.py
    class Article(models.Model):
        ......
        update_time = models.DateTimeField(auto_now=True, verbose_name=u"文章更新时间")
删除 auto_now=True 参数，使文章被访问时阅读量字段计数增加后，文章内容更新时间不受影响，文章内容更新时间则需在后台更新时手动添加。

## 2015-04-22 修正了删除文章同时删除相应配图功能执行失败的问题。

两个错误：

+ models.py 中 Article 类的delete方法中引用的 MEDIA_ROOT 变量有误，已更正。
+ delete 方法中 super() 调用时逻辑位置有误，已更正。

## 2015-04-23 修正了标记为草稿的文章出现在边栏最新文章列表以及url中用文章id直接访问

+ views.py GlobalContextMixin 中 global_context_data['latest'] = Article.objects.all()[:10] 修改为 global_context_data['latest'] = Article.objects.filter(status='0')[:5]
+ ArticleDetailView 试图类中的 get_object() 方法中增加文章对象的 status 字段判断逻辑。
