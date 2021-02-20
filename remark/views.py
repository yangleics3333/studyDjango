from django.shortcuts import render
from remark.models import DjangoTest
from remark.models import AnalysisCommonNews
from django.http import HttpResponse
from django.http import JsonResponse
from django.db.models import Max, Min, Sum, Avg, Count, Q, F

from random import randint

#centos7安装
#yum install gcc mariadb-devel
#pip3 install mysqlclient
# pip install mysqlclient


def handle_insert_save(requests):
    # 增加一条记录，需要适用save()保存
    insert = DjangoTest(title='测试', content='测试内容')
    insert.save()
    return HttpResponse('使用save插入一条数据')


def handle_insert_create(requests):
    # 增加一条数据，不用保存，直接存储
    data = {'title': 'title-01', 'content': 'content-02'}
    DjangoTest.objects.create(**data)

    # DjangoTest.objects.create(title='create_title', content='create_content')
    return HttpResponse('使用create方式插入数据')


def handle_insert_for(requests):
    firsts = "赵,钱,孙,李,周".split(',')
    last = "春,夏,秋,冬,东".split(',')
    items = []
    for data in range(100):
        items.append(DjangoTest(title=firsts[randint(0, 4)] +
                                      last[randint(0, 4)] +
                                      str(randint(111, 999))))
    # 传入一个列表
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


def class_news(request, class_name):
    # between
    # items = AnalysisCommonNews.objects.filter(id__range=[2, 5])

    items = AnalysisCommonNews.objects.filter(news_time__gt='2021-02-08 13:27:00').filter(
        second_class__contains=class_name).filter(is_show=0)
    for data in items:
        # print(data.id, data.title, data.second_class, data.is_show, data.is_check, data.news_time)
        print(data.id, data.similar_id, data.second_class, data.title)
    return HttpResponse('查询新闻数据')


def handle_select(requests):
    # 查询数据
    # all 过滤器 查询所有数据
    data = DjangoTest.objects.all()
    # print(data)  # QuerySet
    items = []
    print(items)
    for i in data:
        items.append(i.title)
    return JsonResponse(items, safe=False, json_dumps_params={'ensure_ascii': False})


def handle_select_where(requests):
    # 查询数据根据where条件
    # data = AnalysisCommonNews.objects.filter(second_class='政策')
    data = AnalysisCommonNews.objects.filter(
        id__gt=44593).filter(article_source='海外网')
    for i in data:
        print(type(i), len(data))
        print(i.id, i.title, i.article_source, i.article_tags)
    return HttpResponse(data)


def handle_select_nested(request):
    # 嵌套查询
    # 只能返回一个value字段不能多个
    items = AnalysisCommonNews.objects.filter(id__gt=2, id__lt=5).values('id')
    data = list(AnalysisCommonNews.objects.filter(id__in=items))
    for i in data:
        print(i.title, i.second_class)
    return HttpResponse('嵌套查询')


def handle_select_count(request):
    # 要引用from django.db.models import Max, Min, Sum, Avg, Count
    count = AnalysisCommonNews.objects.aggregate(Count('id')).get('id__count')
    print(count, type(count))
    return HttpResponse(count)


def handle_select_group(request):
    # similar_id分组内容，id是统计的个数
    # values是分组字典，annotate是统计函数
    # select similar_id,count('id') from analysis_common_news group by similar_id
    res = AnalysisCommonNews.objects.values('similar_id').annotate(Count('id'))
    print(res)
    return HttpResponse(res)


def handle_select_qf(request):
    # Q对象用于多个查询，可以组合
    # & = and
    # | = or
    # ~ = not
    # 主要用于逻辑或，本身filter就是逻辑或
    # items = AnalysisCommonNews.objects.filter(Q(id=2) | Q(id=5) | Q(news_id='d59907f2b1812330ab7876d282b8f220'))
    # 不大于4
    items = AnalysisCommonNews.objects.filter(~Q(id__gte=4))
    for data in items:
        print(data.id, data.similar_id, data.second_class, data.title)
    return HttpResponse('ok')
