# -*- coding:utf8 -*-
"""Airblog 项目的 Django 配置文件。
"""
# 项目基础路径设置
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# 哈希Key
SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


# 项目运行模式
DEBUG = True


# 项目访问控制列表
ALLOWED_HOSTS = ['*']


# 应用注册
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli', # 用于美化 Django admin 后台
    'django.contrib.admin',
    'duoshuo', # 多说应用
    'pagination', # 分页应用
    'blog', # 博客应用
)


# 项目中间件
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware', # 设置 admin 应用中文显示
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware', # 设置分页
)


# 项目根 URL 配置文件
ROOT_URLCONF = 'Airblog.urls'


# 项目 WSGI 应用
WSGI_APPLICATION = 'Airblog.wsgi.application'


# 项目数据库设置
if DEBUG:
    DB_ENGINE = 'django.db.backends.sqlite3'
    DB_NAME = 'airblog.sqlite3'
else:
    DB_ENGINE = 'django.db.backends.mysql'
    DB_NAME = 'Airblog'

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': DB_NAME,
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': '', # sqlite3 不需要
        'PORT': '', # sqlite3 不需要
    }
}


# 语言环境设置
LANGUAGE_CODE = 'zh-cn'


# 时区设置
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# 模板 debug 设置
TEMPLATE_DEBUG = True


# 模板搜索路径
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates/'),
)


# 模版渲染全局变量
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request", # 用于分页应用，其余为默认配置
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
)


# 静态文件设置
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')


# 媒体文件设置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# 日志设置
if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': { # 处理
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(BASE_DIR, 'project.log'),
                'mode': 'a',
            },
        },
        'loggers': { # 日志记录器
            'django.request': {
                'handlers': ['file'],
                'level': 'WARNING',
                'propagate': False,
            },
        },
    }


# duoshuo 设置
DUOSHUO_SECRET = 'xxxxx'
DUOSHUO_SHORT_NAME = 'xxxxx'
