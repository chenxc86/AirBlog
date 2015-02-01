# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6587\u7ae0\u6807\u9898')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6587\u7ae0\u53d1\u5e03\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u6587\u7ae0\u66f4\u65b0\u65f6\u95f4')),
                ('content', models.TextField(verbose_name='\u6587\u7ae0\u5185\u5bb9')),
                ('status', models.CharField(max_length=1, verbose_name='\u6587\u7ae0\u72b6\u6001', choices=[(b'0', '\u53d1\u5e03'), (b'1', '\u8349\u7a3f')])),
                ('heat', models.IntegerField(default=0, verbose_name='\u6587\u7ae0\u9605\u8bfb\u91cf')),
                ('author', models.ForeignKey(verbose_name='\u6587\u7ae0\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-publish_time'],
                'db_table': 'article',
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticleImages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=b'upload_images/%Y/%m/%d', verbose_name='\u6587\u7ae0\u914d\u56fe', blank=True)),
                ('thumb', models.ImageField(upload_to=b'upload_images/thumb_images', verbose_name='\u914d\u56fe\u7f29\u7565\u56fe', blank=True)),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
            options={
                'abstract': False,
                'db_table': 'upload_images',
                'verbose_name': '\u6587\u7ae0\u914d\u56fe',
                'verbose_name_plural': '\u6587\u7ae0\u914d\u56fe',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b\u540d\u79f0')),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u6587\u7ae0\u5206\u7c7b',
                'verbose_name_plural': '\u6587\u7ae0\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag_name', models.CharField(max_length=20, verbose_name='\u6807\u7b7e\u540d\u79f0', blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u6807\u7b7e\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'db_table': 'tag',
                'verbose_name': '\u6587\u7ae0\u6807\u7b7e',
                'verbose_name_plural': '\u6587\u7ae0\u6807\u7b7e',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(verbose_name='\u6587\u7ae0\u5206\u7c7b', to='blog.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6587\u7ae0\u6807\u7b7e', blank=True),
            preserve_default=True,
        ),
    ]
