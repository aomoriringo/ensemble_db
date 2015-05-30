# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CDs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('amazon_url', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Instruments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='MusicCategories',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('order', models.IntegerField(serialize=False, primary_key=True)),
                ('instrument', models.ForeignKey(to='ensemble.Instruments', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('composer_name', models.CharField(max_length=1024)),
                ('composer_name_jp', models.CharField(max_length=1024)),
                ('arranger_name', models.CharField(max_length=1024)),
                ('arranger_name_jp', models.CharField(max_length=1024)),
                ('CD', models.ForeignKey(to='ensemble.CDs')),
            ],
        ),
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('time', models.IntegerField()),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Writers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='works',
            name='arranger',
            field=models.ForeignKey(related_name='work_arrangers', to='ensemble.Writers', null=True),
        ),
        migrations.AddField(
            model_name='works',
            name='composer',
            field=models.ForeignKey(related_name='work_composers', to='ensemble.Writers'),
        ),
        migrations.AddField(
            model_name='works',
            name='parent',
            field=models.ForeignKey(to='ensemble.Works', null=True),
        ),
        migrations.AddField(
            model_name='tracks',
            name='work',
            field=models.ForeignKey(to='ensemble.Works', null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='work',
            field=models.ForeignKey(to='ensemble.Works', unique=True),
        ),
        migrations.AddField(
            model_name='instruments',
            name='instrument_type',
            field=models.ForeignKey(to='ensemble.InstrumentTypes'),
        ),
    ]
