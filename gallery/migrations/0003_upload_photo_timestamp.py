# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20171217_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload_photo',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 12, 16, 20, 56, 23, 382539, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
