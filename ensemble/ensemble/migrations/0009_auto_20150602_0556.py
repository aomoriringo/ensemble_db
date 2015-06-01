# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0008_auto_20150602_0553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workmusiccategory',
            name='number',
        ),
        migrations.RemoveField(
            model_name='workmusiccategory',
            name='parent',
        ),
        migrations.AddField(
            model_name='musiccategory',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='musiccategory',
            name='parent',
            field=models.ForeignKey(blank=True, to='ensemble.MusicCategory', null=True),
        ),
    ]
