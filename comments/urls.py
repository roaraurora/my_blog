# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: deeeeeeeee
# @Date  : 2018/3/18
from django.urls import path
from comments import views

app_name = 'comments'

urlpatterns = [
    path(r'comment/post/<int:post_pk>/', views.post_comment, name='post_comment'),
]