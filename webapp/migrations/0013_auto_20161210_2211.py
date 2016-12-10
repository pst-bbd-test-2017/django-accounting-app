# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 22:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_auto_20161210_2209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='tax_id',
        ),
        migrations.AddField(
            model_name='invoiceline',
            name='tax_id',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='webapp.Tax'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='date_invoice',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 10, 22, 11, 8, 916775, tzinfo=utc), verbose_name='Date'),
        ),
    ]
