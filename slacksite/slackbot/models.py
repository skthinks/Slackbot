from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30)
    user_id = models.CharField(max_length=30)


class Leaderboards(models.Model):
    user_id = models.CharField(max_length=30)
    leave_early = models.IntegerField()
    arrive_late = models.IntegerField()
    on_leave = models.IntegerField()
