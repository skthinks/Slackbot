# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 11:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slackbot', '0004_auto_20160611_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offence_log',
            old_name='user',
            new_name='user_id',
        ),
    ]
