# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-14 07:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0027_auto_20161214_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='date_invoice',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 14, 7, 57, 40, 505301, tzinfo=utc), verbose_name='Date'),
        ),
    ]