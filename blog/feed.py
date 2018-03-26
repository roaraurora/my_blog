# -*- coding: utf-8 -*-
# @File  : feed.py
# @Author: deeeeeeeee
# @Date  : 2018/3/20
from django.contrib.syndication.views import Feed
from .models import Post


class AllPostsRssFeed(Feed):
    title = "Roar blog"
    link = '/'
    description = "o wait what is this"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body



