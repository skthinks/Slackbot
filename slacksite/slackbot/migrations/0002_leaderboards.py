# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slackbot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaderboards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('leave_early', models.IntegerField()),
                ('arrive_late', models.IntegerField()),
                ('on_leave', models.IntegerField()),
            ],
        ),
    ]