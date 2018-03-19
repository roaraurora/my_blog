# -*- coding: utf-8 -*-
# @File  : forms.py
# @Author: deeeeeeeee
# @Date  : 2018/3/18
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']