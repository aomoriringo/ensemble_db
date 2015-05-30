# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('order', models.IntegerField(serialize=False, primary_key=True)),
                ('instrument', models.ForeignKey(to='ensemble.Instrument', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('composer_name', models.CharField(max_length=1024)),
                ('composer_name_jp', models.CharField(max_length=1024)),
                ('arranger_name', models.CharField(max_length=1024)),
                ('arranger_name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('time', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='CDs',
            new_name='CD',
        ),
        migrations.RenameModel(
            old_name='Writers',
            new_name='InstrumentType',
        ),
        migrations.RenameModel(
            old_name='MusicCategories',
            new_name='MusicCategory',
        ),
        migrations.RenameModel(
            old_name='InstrumentTypes',
            new_name='Writer',
        ),
        migrations.RemoveField(
            model_name='instruments',
            name='instrument_type',
        ),
        migrations.RemoveField(
            model_name='players',
            name='instrument',
        ),
        migrations.RemoveField(
            model_name='players',
            name='work',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='CD',
        ),
        migrations.RemoveField(
            model_name='tracks',
            name='work',
        ),
        migrations.RemoveField(
            model_name='works',
            name='arranger',
        ),
        migrations.RemoveField(
            model_name='works',
            name='composer',
        ),
        migrations.RemoveField(
            model_name='works',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Instruments',
        ),
        migrations.DeleteModel(
            name='Players',
        ),
        migrations.DeleteModel(
            name='Tracks',
        ),
        migrations.DeleteModel(
            name='Works',
        ),
        migrations.AddField(
            model_name='work',
            name='arranger',
            field=models.ForeignKey(related_name='work_arrangers', to='ensemble.Writer', null=True),
        ),
        migrations.AddField(
            model_name='work',
            name='composer',
            field=models.ForeignKey(related_name='work_composers', to='ensemble.Writer'),
        ),
        migrations.AddField(
            model_name='work',
            name='parent',
            field=models.ForeignKey(to='ensemble.Work', null=True),
        ),
        migrations.AddField(
            model_name='track',
            name='CD',
            field=models.ForeignKey(to='ensemble.CD'),
        ),
        migrations.AddField(
            model_name='track',
            name='work',
            field=models.ForeignKey(to='ensemble.Work', null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='work',
            field=models.ForeignKey(to='ensemble.Work', unique=True),
        ),
        migrations.AddField(
            model_name='instrument',
            name='instrument_type',
            field=models.ForeignKey(to='ensemble.InstrumentType'),
        ),
    ]
