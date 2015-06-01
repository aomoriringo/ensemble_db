# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0003_auto_20150602_0423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='subtitle',
            new_name='short_title',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='subtitle_jp',
            new_name='short_title_jp',
        ),
        migrations.RenameField(
            model_name='work',
            old_name='title_jp_reading',
            new_name='short_title_jp_reading',
        ),
        migrations.AddField(
            model_name='playerinstrument',
            name='override_description',
            field=models.CharField(max_length=1024, blank=True),
        ),
    ]
