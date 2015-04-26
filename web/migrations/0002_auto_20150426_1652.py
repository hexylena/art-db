# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='depth',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='depth_units',
            field=models.CharField(default='cm', max_length=2, choices=[(b'm', b'meters'), (b'cm', b'centimeters'), (b'f', b'feet'), (b'i', b'inches')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='finished',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='artwork',
            name='height',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='height_units',
            field=models.CharField(default='cm', max_length=2, choices=[(b'm', b'meters'), (b'cm', b'centimeters'), (b'f', b'feet'), (b'i', b'inches')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='mass',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='mass_units',
            field=models.CharField(default='kg', max_length=2, choices=[(b'kg', b'kilograms'), (b'lb', b'pounds')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='width',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artwork',
            name='width_units',
            field=models.CharField(default='cm', max_length=2, choices=[(b'm', b'meters'), (b'cm', b'centimeters'), (b'f', b'feet'), (b'i', b'inches')]),
            preserve_default=False,
        ),
    ]
