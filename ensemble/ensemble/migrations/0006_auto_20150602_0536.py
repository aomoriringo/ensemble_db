# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0005_auto_20150602_0528'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movement',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='cd',
            name='amazon_url',
        ),
        migrations.AddField(
            model_name='cd',
            name='asin',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='movement',
            name='title_jp',
            field=models.CharField(default=b'', max_length=1024),
        ),
    ]
