# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0016_auto_20150605_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreshop',
            name='publisher',
        ),
    ]
