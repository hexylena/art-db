# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_artworkview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artwork',
            name='depth_units',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='height_units',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='mass_units',
        ),
        migrations.RemoveField(
            model_name='artwork',
            name='width_units',
        ),
        migrations.AlterField(
            model_name='artworkview',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]
