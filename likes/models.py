from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()  # 主键ID
    content_object = GenericForeignKey('content_type', 'object_id')  # 通用外键

    liked_num = models.IntegerField(default=0)

class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()  # 主键ID
    content_object = GenericForeignKey('content_type', 'object_id')  # 通用外键

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_time = models.DateTimeField(auto_now_add=True)

