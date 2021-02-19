from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(requests):
    name = 'yanglei'
    return render(requests, "group/index.html", context=locals())


def home(requests):
    return render(requests, "group/home.html")


def load_templates(requests):
    # 原理步骤
    # 加载模板文件，生成渲染对象
    """
    obj = loader.get_template("group/load_template.html")
    print(obj, type(obj))
    print(obj.__dict__)
    res = obj.render({"name": "rock-yanglei"})
    print(res, type(res))
    return HttpResponse(res)
    """
    # 更加简单的方式
    # 必传的三个参数：
    # 1、请求对象requests
    # 2、模板名称
    # 3、参数（字段）
    return render(requests, "group/load_template.html", context={"name": "yanng-rock"})

#变量
def handle_var(requests):
    num = 10
    name = "中国"
    students = [10,20,30,40]
    student = {"name":"rock","age":30}
    return render(requests,"group/var_content.html",context=locals())

#过滤
def handle_filter(requests):
    num = 10
    name = "中国"
    return render(requests,"group/filter.html",locals())