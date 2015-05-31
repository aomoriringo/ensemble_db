# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024)),
                ('amazon_url', models.URLField(max_length=10000)),
                ('release', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='InstrumentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='MusicCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('number', models.IntegerField()),
                ('instrument', models.ForeignKey(to='ensemble.Instrument')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
                ('url', models.URLField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amazon_url', models.URLField(max_length=10000, blank=True)),
                ('pubulisher', models.ForeignKey(to='ensemble.Publisher')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('title', models.CharField(max_length=1024, blank=True)),
                ('title_jp', models.CharField(max_length=1024, blank=True)),
                ('composer_name', models.CharField(max_length=1024, blank=True)),
                ('composer_name_jp', models.CharField(max_length=1024, blank=True)),
                ('arranger_name', models.CharField(max_length=1024, blank=True)),
                ('arranger_name_jp', models.CharField(max_length=1024, blank=True)),
                ('CD', models.ForeignKey(to='ensemble.CD')),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1024)),
                ('title_jp', models.CharField(max_length=1024, blank=True)),
                ('title_jp_reading', models.CharField(max_length=1024, blank=True)),
                ('subtitle', models.CharField(max_length=1024, blank=True)),
                ('subtitle_jp', models.CharField(max_length=1024, blank=True)),
                ('time_minute', models.IntegerField(null=True, blank=True)),
                ('time_second', models.IntegerField(null=True, blank=True)),
                ('order', models.IntegerField(null=True, blank=True)),
                ('parent', models.ForeignKey(blank=True, to='ensemble.Work', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkArranger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkComposer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkMusicCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('music_category', models.ForeignKey(to='ensemble.MusicCategory')),
                ('work', models.ForeignKey(to='ensemble.Work')),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_reading', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
                ('name_jp_reading', models.CharField(max_length=1024)),
            ],
        ),
        migrations.AddField(
            model_name='workcomposer',
            name='composer',
            field=models.ForeignKey(to='ensemble.Writer'),
        ),
        migrations.AddField(
            model_name='workcomposer',
            name='work',
            field=models.ForeignKey(to='ensemble.Work'),
        ),
        migrations.AddField(
            model_name='workarranger',
            name='arranger',
            field=models.ForeignKey(to='ensemble.Writer'),
        ),
        migrations.AddField(
            model_name='workarranger',
            name='work',
            field=models.ForeignKey(to='ensemble.Work'),
        ),
        migrations.AddField(
            model_name='track',
            name='work',
            field=models.ForeignKey(blank=True, to='ensemble.Work', null=True),
        ),
        migrations.AddField(
            model_name='score',
            name='work',
            field=models.ForeignKey(to='ensemble.Work'),
        ),
        migrations.AddField(
            model_name='player',
            name='work',
            field=models.ForeignKey(to='ensemble.Work'),
        ),
        migrations.AddField(
            model_name='instrument',
            name='instrument_type',
            field=models.ForeignKey(to='ensemble.InstrumentType'),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('work', 'order', 'instrument')]),
        ),
    ]
