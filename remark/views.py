# -*- coding: <encoding name> -*-
from django.shortcuts import render
from remark.models import DjangoTest
from remark.models import AnalysisCommonNews
from django.http import HttpResponse
from django.http import JsonResponse
from random import randint
#pip install mysqlclient

def handle_insert_save(requests):
    # 增加一条记录，需要适用save()保存
    insert = DjangoTest(title='测试', content='测试内容')
    insert.save()
    return HttpResponse('使用save插入一条数据')


def handle_insert_create(requests):
    # 增加一条数据，不用保存，直接存储
    data = {'title': 'title-01', 'content': 'content-02'}
    DjangoTest.objects.create(**data)

    #DjangoTest.objects.create(title='create_title', content='create_content')
    return HttpResponse('使用create方式插入数据')


def handle_insert_for(requests):
    firtst = "赵,钱,孙,李,周".split(',')
    last = "春,夏,秋,冬,东".split(',')
    items = []
    for data in range(100):
        items.append(DjangoTest(title=firtst[randint(0, 4)] +
                                last[randint(0, 4)] +
                                str(randint(111, 999))))
    DjangoTest.objects.bulk_create(items)
    return HttpResponse('适用for批量插入')


def handle_insert_bulk_create(requests):
    # 批量插入数据
    DjangoTest.objects.bulk_create([DjangoTest.objects.create(title='create_title1', content='create_content1'),
                                    DjangoTest.objects.create(
        title='create_title2', content='create_content2'),
        DjangoTest.objects.create(
        title='create_title3', content='create_content3'),
        DjangoTest.objects.create(
        title='create_title4', content='create_content4'),
        DjangoTest.objects.create(
        title='create_title5', content='create_content5'),
        DjangoTest.objects.create(
        title='create_title6', content='create_content6'),
        DjangoTest.objects.create(
        title='create_title7', content='create_content7'),
        DjangoTest.objects.create(title='create_title8', content='create_content8')])
    return HttpResponse('使用bulk create方式插入数据')


def handle_delete(requests):
    # 删除一条
    try:
        data = DjangoTest.objects.get(pk=38704)
        print(data, type(data))

        if data:
            data.delete()
    except Exception as e:
        print(e)
    return HttpResponse('删除一条数据')


def handle_delete_bulk(requests):
    # 批量删除
    try:
        data = DjangoTest.objects.filter(id_gte=38792)
        print(data)
        data.delete()
    except Exception as e:
        print(e)
    return HttpResponse('删除一条数据')


def handle_update(requests):
    # 更新一条记录
    data = DjangoTest.objects.get(pk=38702)
    data.title = '测试的修改'
    data.save()
    return HttpResponse('更新一条数据')


def handle_update_bulk(requests):
    # 批量更新
    data = DjangoTest.objects.all()
    data.update(title='1')
    return HttpResponse('批量更新字段数据')


def handle_select(requests):
    # 查询数据
    # all 过滤器 查询所有数据
    data = DjangoTest.objects.all()
    print(data)  # QuerySet
    for i in data:
        print(i.title)
    return HttpResponse('查询数据')


def hanle_select_where(requests):
    # 查询数据根据where条件
    #data = AnalysisCommonNews.objects.filter(second_class='政策')
    data = AnalysisCommonNews.objects.filter(
        id__gt=44593).filter(article_source='海外网')
    for i in data:
        print(i.id, i.title, i.article_source, i.article_tags)
    return HttpResponse('where查询数据')
