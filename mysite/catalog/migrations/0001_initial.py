# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pid', models.CharField(max_length=200)),
                ('Pname', models.CharField(max_length=200)),
                ('Ppicture', models.CharField(max_length=200)),
                ('Pbrand', models.CharField(max_length=200)),
                ('Ptype', models.CharField(max_length=200)),
                ('Pprice', models.FloatField()),
                ('Pamount', models.FloatField()),
                ('Pdetail', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
