# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0002_auto_20150602_0406'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerInstrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('instrument', models.ForeignKey(to='ensemble.Instrument')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('work', 'order')]),
        ),
        migrations.AddField(
            model_name='playerinstrument',
            name='player',
            field=models.ForeignKey(to='ensemble.Player'),
        ),
        migrations.RemoveField(
            model_name='player',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='player',
            name='number',
        ),
    ]
