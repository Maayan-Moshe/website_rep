# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:41:40 2015

@author: mmoshe
"""

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(/?P<blog_name>+/?P<page_name>+$', views.blog_page_display, name='index'),
]