from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=30)
    user_name = models.CharField(max_length=30)


class OffenceLog(models.Model):
    user = models.ForeignKey('User')
    timestamp = models.DateField(auto_now_add=True)
    offence_type = models.CharField(max_length=30)
