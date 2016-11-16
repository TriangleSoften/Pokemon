# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='CustID',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='Pname',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='Ppicture',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cartitem',
            name='username',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]
