# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0018_auto_20150609_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='musiccategory',
            name='name_jp_short',
            field=models.CharField(default='', max_length=1024),
            preserve_default=False,
        ),
    ]
