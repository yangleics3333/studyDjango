#!/usr/bin/env python3
# coding:utf-8

from django.urls import path
from remark import views

app_name = "Remark"  # 应用的命名空间,用于反向查询

urlpatterns = [
    path('insertSave/', views.handle_insert_save, name='insertSave'),
    path('insertCreate/', views.handle_insert_create, name='insertCreate'),
    path('insertBulkCreate/', views.handle_insert_bulk_create, name='insertBulkCreate'),
    path('insertFor/', views.handle_insert_for, name='insertFor'),
    path('update/', views.handle_update, name='update'),
    path('updateBulk/', views.handle_update_bulk, name='updateBulk'),
    path('delete/', views.handle_delete, name='delete'),
    path('deleteBulk/', views.handle_delete_bulk, name='deleteBulk'),
    path('classNews/<class_name>/', views.class_news, name='classNews'),
    path('select/', views.handle_select, name='select'),
    path('selectWhere/', views.handle_select_where, name='selectWhere'),
    path('selectNested/', views.handle_select_nested, name='selectNested'),
    path('selectCount/', views.handle_select_count, name='selectCount'),
    path('selectGroup/', views.handle_select_group, name='selectGroup'),
    path('selectQF/', views.handle_select_qf, name='selectQF'),
]
