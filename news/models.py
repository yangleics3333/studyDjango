from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    class Meta:
        db_table = 'users' #指定表明