# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='writer',
            name='name_reading',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
