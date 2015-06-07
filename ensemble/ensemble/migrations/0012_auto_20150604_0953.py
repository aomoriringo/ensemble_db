# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0011_auto_20150602_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='title',
            field=models.CharField(default=b'', max_length=1024),
        ),
    ]
