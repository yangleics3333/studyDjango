from django.db import models

# Create your models here.
# 类 - 表
# 对象 - 记录（一行）
# 属性 - 字段（属性，列）

# 自己的模型必须继承Model，不继承无法访问数据库

#适用inspectdb > remark/models_dev.py 来进行反向生成，先建表在生成
class SpiderWsNews(models.Model):
    # db_column 指明表中的字段名
    news_id = models.CharField(max_length=32)
    # Charfield 必须适用max_length指明长度，其他类型可以不给。
    title = models.CharField(max_length=700)
    content = models.TextField()
    # auto_now是每次保存对象时，自动设置该字段当前时间
    # auto_now_add是第一次创建是设置时间。
    news_time = models.DateTimeField(auto_now_add=True)

    #元数据
    # 可以设置表的信息，也叫模型本身的信息
    class Meta:
        #默认表名：应用名 模型名
        db_table = 'spider_ws_news'
        ordering = ['news_time'] #按照news_time进行排序，不设置的话按照id主键排序
        