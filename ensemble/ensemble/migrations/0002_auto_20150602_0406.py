# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='amazon_url',
        ),
        migrations.AddField(
            model_name='score',
            name='asin',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
