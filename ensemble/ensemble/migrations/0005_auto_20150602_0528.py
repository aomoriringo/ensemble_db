# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0004_auto_20150602_0527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='work',
            name='order',
        ),
        migrations.RemoveField(
            model_name='work',
            name='parent',
        ),
        migrations.AddField(
            model_name='movement',
            name='work',
            field=models.ForeignKey(to='ensemble.Work'),
        ),
    ]
