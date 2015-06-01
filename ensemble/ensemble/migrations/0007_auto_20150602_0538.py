# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0006_auto_20150602_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='time_minute',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='movement',
            name='time_second',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
