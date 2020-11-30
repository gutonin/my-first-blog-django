# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Post
from django.shortcuts import render

def post_list(request):
    return render (request, 'blog/post_list.html', {})
