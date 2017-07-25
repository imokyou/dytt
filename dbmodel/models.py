# coding=utf-8
from django.db import models


class Video(models.Model):
    uid = models.CharField(max_length=32)
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=512)
    section = models.IntegerField()
    category = models.IntegerField()
    pubdate = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'video'

    SECITON2NAME = {
        0: '新片精品',
        1: '必看热片',
        2: '迅雷电影资源',
        3: '六月经典大片',
        4: '华语电视剧',
        5: '日韩电视剧',
        6: '欧美电视剧',
        7: '综艺&动漫'
    }

