# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-27 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20161115_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='Pname',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='Ppicture',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='Pprice',
        ),
    ]
