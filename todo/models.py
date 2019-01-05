import datetime

from django.db import models

# Create your models here.
from django.utils import timezone


class Task(models.Model):
    task_text = models.CharField('任务', max_length=200)
    create_date = models.DateTimeField('创建时间')

    def was_created_recently(self):
        now = timezone.now()
        return now >= self.create_date >= now - datetime.timedelta(days=2)

    was_created_recently.admin_order_field = 'create_date'
    was_created_recently.boolean = True
    was_created_recently.short_description = '近期创建'

    def __str__(self):
        return self.task_text
