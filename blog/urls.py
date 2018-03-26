# -*- coding: utf-8 -*-
# @File  : urls.py
# @Author: deeeeeeeee
# @Date  : 2018/3/17

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'post/<int:pk>', views.PostDetailView.as_view(), name='detail'),
    path(r'archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives'),
    path(r'category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path(r'tag/<int:pk>/', views.TagView.as_view(), name='tag'),
]