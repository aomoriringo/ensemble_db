# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0014_auto_20150605_0406'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='publisher',
            new_name='score_publisher',
        ),
        migrations.AddField(
            model_name='score',
            name='url',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
