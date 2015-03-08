# -*- coding:utf8 -*-
"""
Author: Chenxc
Date: 2015/01/18
"""
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from django.contrib.auth.models import User
import os
from django.conf import settings
from utils.image_toolkit import make_thumb, del_image


class Category(models.Model):
    """文章分类模型
    """
    # 分类名称
    name = models.CharField(max_length=20, verbose_name=u"分类名称")

    def __unicode__(self):
        return u"%s" % (self.name)

    class Meta:
        """模型元数据
        """
        # 数据库表名
        db_table = "category"
        # 对象可视化名称，如果verbose_name_plural为定义，则按verbose_name + "s"显示
        verbose_name_plural = verbose_name = u"文章分类"


class Tag(models.Model):
    """文章标签模型
    """
    # 标签名称
    tag_name = models.CharField(max_length=20, verbose_name=u"标签名称", blank=True)
    # 标签创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name=u"标签创建时间")

    def __unicode__(self):
        return u"%s" % (self.tag_name)

    class Meta:
        db_table = "tag"
        verbose_name_plural = verbose_name = u"文章标签"


class Article(models.Model):
    """文章模型
    """
    # 文章状态
    STATUS = (("0", u"发布"), ("1", u"草稿"))

    # 文章标
    title = models.CharField(max_length=50, verbose_name=u"文章标题")
    # 文章作者
    author = models.ForeignKey(User, verbose_name=u"文章作者")
    # 文章分类
    category = models.ForeignKey(Category, verbose_name=u"文章分类")
    # 文章标签
    tag = models.ManyToManyField(Tag, verbose_name=u"文章标签", blank=True)
    # 文章发布时间
    publish_time = models.DateTimeField(auto_now_add=True, verbose_name=u"文章发布时间")
    # 文章最后更新时间
    update_time = models.DateTimeField(verbose_name=u"文章更新时间")
    # 文章内容
    content = models.TextField(verbose_name=u"文章内容")
    # 文章状态
    status = models.CharField(max_length=1, choices=STATUS, verbose_name=u"文章状态")
    # 文章阅读量
    heat = models.IntegerField(default=0, verbose_name=u"文章阅读量")

    def delete(self):
        """删除文章的同时删除文件系统中相关联的图片
        """
        images_of_article = self.articleimages_set.all()
        if images_of_article:
            for image_of_article in images_of_article:
                del_image(os.path.join(MEDIA_ROOT, image_of_article.image.name))
                if image_of_article.thumb:
                    del_image(os.path.join(MEDIA_ROOT, image_of_article.thumb.name))
                super(Article, self).delete()
        else:
            super(Article, self).delete()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        db_table = "article"
        verbose_name_plural = verbose_name = u"文章"
        # 按发布时间倒序排列
        ordering = ['-publish_time',]


class Media(models.Model):
    """文章媒体超类
    """
    # 上传时间
    upload_time = models.DateTimeField(auto_now_add=True)
    # 关联的文章
    article = models.ForeignKey(Article)

    class Meta:
        # 定义 Media 为抽象类，只用于被子类继承
        abstract = True


class ArticleImages(Media):
    """文章配图
    """
    # 上传图片的URL
    image = models.ImageField(upload_to='upload_images/%Y/%m/%d', verbose_name=u"文章配图", blank=True)
    # 图片缩略图的URL
    thumb = models.ImageField(upload_to='upload_images/thumb_images', verbose_name=u"配图缩略图", blank=True)

    def __unicode__(self):
        return u'%s %s' % (self.image.name, self.article.title)

    def save(self, *args, **kwargs):
        """存储数据同时生成图片缩略
        """
        base, ext = os.path.splitext(os.path.basename(self.image.path))
        super(ArticleImages, self).save()
        thumb_buf = make_thumb(self.image.path)
        if thumb_buf:
            relate_thumb_path = os.path.join('upload_images/thumb_images', base + '.thumb' + ext)
            thumb_path = os.path.join(settings.MEDIA_ROOT, relate_thumb_path)
            thumb_buf.save(thumb_path)
            self.thumb = ImageFieldFile(self, self.thumb, relate_thumb_path)
            super(ArticleImages, self).save()

    class Meta(Media.Meta):
        db_table = "upload_images"
        verbose_name_plural = verbose_name = u"文章配图"
