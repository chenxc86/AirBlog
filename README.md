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
