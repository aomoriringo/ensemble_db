# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0009_auto_20150602_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
