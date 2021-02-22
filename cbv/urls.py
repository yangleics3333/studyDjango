#!/usr/bin/env python3
# coding:utf-8

from django.urls import path
from cbv import views

app_name = "Cbv"  # 应用的命名空间,用于反向查询

urlpatterns = [
    path('req/',views.NewsView.as_view(),name = 'req')
]
