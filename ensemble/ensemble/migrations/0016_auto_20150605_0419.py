# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0015_auto_20150605_0408'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asin', models.CharField(max_length=10, blank=True)),
                ('url', models.CharField(max_length=1024, blank=True)),
                ('CD', models.ForeignKey(to='ensemble.CD')),
                ('shop', models.ForeignKey(blank=True, to='ensemble.Shop', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreShop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('asin', models.CharField(max_length=10, blank=True)),
                ('url', models.CharField(max_length=1024, blank=True)),
                ('publisher', models.ForeignKey(to='ensemble.Publisher')),
                ('shop', models.ForeignKey(blank=True, to='ensemble.Shop', null=True)),
                ('work', models.ForeignKey(to='ensemble.Work')),
            ],
        ),
        migrations.RemoveField(
            model_name='score',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='score',
            name='work',
        ),
        migrations.DeleteModel(
            name='Score',
        ),
    ]
