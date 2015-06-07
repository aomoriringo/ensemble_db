# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0013_auto_20150604_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1024)),
                ('name_jp', models.CharField(max_length=1024)),
                ('url', models.URLField(max_length=10000)),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='publisher',
            field=models.ForeignKey(blank=True, to='ensemble.Publisher', null=True),
        ),
    ]
