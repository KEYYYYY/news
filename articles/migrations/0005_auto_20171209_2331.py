# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20171209_2330'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-add_time',), 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
    ]