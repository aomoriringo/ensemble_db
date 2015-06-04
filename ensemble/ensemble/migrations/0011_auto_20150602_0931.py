# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0010_auto_20150602_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='score',
            old_name='pubulisher',
            new_name='publisher',
        ),
    ]
