# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-20 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20160425_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='e-mail')),
                ('telephone', models.IntegerField(max_length=11)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
    ]