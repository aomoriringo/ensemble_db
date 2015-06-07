# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0012_auto_20150604_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movement',
            name='title',
            field=models.CharField(default=b'', max_length=1024, blank=True),
        ),
        migrations.AlterField(
            model_name='movement',
            name='title_jp',
            field=models.CharField(default=b'', max_length=1024, blank=True),
        ),
    ]
