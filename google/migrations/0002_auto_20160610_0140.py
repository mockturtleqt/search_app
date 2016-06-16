# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 22:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='keyword',
            name='url',
        ),
        migrations.AddField(
            model_name='url',
            name='keyword',
            field=models.ManyToManyField(to='google.Keyword'),
        ),
    ]
