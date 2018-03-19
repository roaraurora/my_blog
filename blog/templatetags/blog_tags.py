# -*- coding: utf-8 -*-
# @File  : blog_tags.py
# @Author: deeeeeeeee
# @Date  : 2018/3/18
from ..models import Post, Category
from django import template

register = template.Library()


@register.simple_tag
def get_recent_post(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_category():
    return Category.objects.all()