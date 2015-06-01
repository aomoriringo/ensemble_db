# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0007_auto_20150602_0538'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='short_name',
            field=models.CharField(max_length=1024, blank=True),
        ),
        migrations.AddField(
            model_name='workmusiccategory',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='workmusiccategory',
            name='parent',
            field=models.ForeignKey(blank=True, to='ensemble.WorkMusicCategory', null=True),
        ),
        migrations.AlterField(
            model_name='playerinstrument',
            name='number',
            field=models.IntegerField(default=1),
        ),
    ]
