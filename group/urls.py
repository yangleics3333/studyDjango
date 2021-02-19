#!/usr/bin/env python3
# coding:utf-8

from django.urls import path
from group import views

app_name = "Group"  # 应用的命名空间

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("loadTemplates/", views.load_templates, name="loadTemplates"),
    path("handleVar/", views.handle_var, name="handle_var"),
    path("handleFilter/", views.handle_filter, name="handle_filter")
]
