# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-11 17:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_auto_20161211_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_invoice',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 11, 17, 50, 15, 364663, tzinfo=utc), verbose_name='Date'),
        ),
    ]
