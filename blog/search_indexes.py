# -*- coding: utf-8 -*-
# @File  : search_indexes.py
# @Author: deeeeeeeee
# @Date  : 2018/3/20
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()