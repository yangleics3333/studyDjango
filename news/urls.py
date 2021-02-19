#!/usr/bin/env python3
#coding:utf-8

from django.urls import path
from news import views

app_name = "News" #应用的命名空间

urlpatterns = [
    path('',views.index,name ='index'),
    path('home/',views.home,name ='home'),
    #整数类型
    path('show/<int:age>/',views.show,name='show'),
    #slug:只能传入数字、字母、-和_组成的字符串参数
    path('list/<slug:name>',views.list_user,name='list_user'),
    #path匹配任何非空字符串包括/
    path('access/<path:path>/',views.access,name='access'),
    #string类型
    path('change/<name>/',views.change_name,name='change'),
    #传入多个值
    path('player/<name>/<int:age>/',views.player,name = 'player'),
    path('getReq/',views.get_req,name='getReq'),
    path('postReq/',views.post_req,name='postReq'),
    path('reqInfo/',views.req_info,name='reqInfo'),
    path('renderInfo/',views.render_info,name='renderInfo'),
    path('jsonInfo/',views.json_info,name='jsonInfo'),
    path('redirect/',views.redirect1,name='redirect'),
    path('redq/',views.redq,name='redq'),
    path('baidu/',views.baidu,name='baidu'),
    path('reversePath/',views.reverse_path,name='reversePath'),
    path('reversePathPara/',views.reverse_path_para,name='reversePathPara'),
]