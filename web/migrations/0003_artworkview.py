# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20150426_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtworkView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to='images', blank=True)),
                ('artwork', models.ForeignKey(to='web.Artwork')),
            ],
        ),
    ]
