# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-16 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=120)),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
