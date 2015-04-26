# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20150426_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='depth',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='height',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='mass',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='artwork',
            name='width',
            field=models.CharField(max_length=20),
        ),
    ]
