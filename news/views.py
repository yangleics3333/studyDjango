#!/usr/bin/env python3
# coding:utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from news.models import User


def index(request):
    return HttpResponse("index - hello world")


def home(request):
    # 查询数据库
    users = User.objects.all()
    return render(request, "news/index.html", context={"title": "yanng - index", "name": "rock1", 'users': users})
    # return HttpResponse("home - 首页")


def show(requests, age):
    print(age)
    print(type(age))
    return HttpResponse(str(age))


def list_user(requests, name):
    print(name, type(name))
    return HttpResponse(name)


def access(requests, path):
    # path 可以包含任何字符
    return HttpResponse(path)


def change_name(requests, name):
    return HttpResponse(name + '- 123')


def player(requests, name, age):
    return HttpResponse(name + str(age))


# 使用get方法请求
def get_req(requests):
    print(requests.method)
    print(requests.GET)
    name = requests.GET.get('name')  # 获取单一值 get
    print(name)
    print(type(name))

    age = requests.GET.getlist('age')  # 获取多个值 getlist ,返回一个列表['10', '20']
    print(age)
    print(type(age))
    return HttpResponse(name + str(age))


def post_req(requests):
    print(requests.method)
    name = requests.POST.get('name')  # 获取单一值 get
    age = requests.POST.getlist('age')  # 获取多个值 getlist ,返回一个列表['10', '20']
    print(name)
    print(age)
    return HttpResponse('task end!')


def req_info(requests):
    print(requests.method)  # 请求方式
    print(requests.path)  # 相对路径/news/reqInfo/
    print(requests.META)  # 用户请求字典
    print(requests.META.get('REMOTE_ADDR'))  # 客户端地址
    print(requests.META.get('REMOTE_HOST'))  # 客户端主机
    print(requests.get_full_path())  # /news/reqInfo/
    print(requests.get_host())  # 127.0.0.1:8000
    print(requests.build_absolute_uri())  # 绝对访问地址http://127.0.0.1:8000/news/reqInfo/

    print(requests.GET)  # django中的QueryDict   -<QueryDict: {}>
    print(requests.GET.dict())  # python中的dick  -{}
    return HttpResponse('req_info')


def res_info(requests):
    res = HttpResponse('res_info')
    res.content_type = "text/html"
    res.status_code = 400
    return res


def render_info(requests):
    # 调用模板返回
    # render渲染之后也是通过HttpResponse返回
    # 使用render有三个参数：
    # 1、requests
    # 2、模板名称
    # 3、参数(渲染的变量)
    return render(requests, "render.html", context={"title": "render task", "name": "yanglei"})


def json_info(requests):
    content = {"name": "yanglei",
               "age": 18,
               "sex": "male"}
    list_con = [{"name": "yanglei", "age": 18, "sex": "male"},
                {"name": "tanzheng", "age": 28, "sex": "female"}]
    # return JsonResponse(content)
    return JsonResponse(list_con, safe=False)  # 字典需要将safe设置未False，默认未True


# 重定向
def redirect1(requests):
    # 首先用HttpResponseRedirect
    # 使用HttpResponseRedirect将重庆想的路径设置
    # 弊端：太长了
    return HttpResponseRedirect("/news/show/{}/".format(10))


def redq(requests):
    return HttpResponseRedirect("/news/player/{}/{}/".format("rock", 10))


def baidu(requests):
    return HttpResponseRedirect('https://www.baidu.com/')


# 反向定位
# 由应用的作用域（命名空间）：name来确定路由
# 首先在应用下的urls.py中进行设置
# 反向定位是根据命名空间:name名，来找到请求路径
# 正向是请求路径到函数
# 需要导入包 ： from django.urls import reverse
def reverse_path(requests):
    return HttpResponseRedirect(reverse("News:jsonInfo"))


# 带参数的：
# 路径中具体名字的必须用
# kwargs = {'age':1}
def reverse_path_para(requests):
    return HttpResponseRedirect(reverse("News:player", kwargs={'name': 'rock', 'age': 1000}))

# 视图错误
# 403错误：permission_denied - 权限拒绝
# 404错误：page_not_found - 找不到指定文件
# 500错误：server_error - 服务器内部错误

# Debug模式关闭下定义404页面
