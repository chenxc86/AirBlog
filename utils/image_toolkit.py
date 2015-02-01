# -*- coding:utf8 -*-
"""
Author: Chenxc
Date: 2015/01/18
"""
import os
from PIL import Image


def make_thumb(path, size=600):
    """为上传的图片生成缩略
    """
    image_buf = Image.open(path)
    width, height = image_buf.size
    if width > size:
        delta = width / size
        height = int(height / delta)
        image_buf.thumbnail((size, height), Image.ANTIALIAS)
#        image_buf.resize((size, height), Image.ANTIALIAS)
        return image_buf


def del_image(path):
    """删除文章配图
    """
    if os.path.isfile(path):
         os.remove(path)
