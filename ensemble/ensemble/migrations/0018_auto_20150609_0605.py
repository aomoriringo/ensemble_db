# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ensemble', '0017_remove_scoreshop_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='instrument',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='instrumenttype',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='musiccategory',
            options={'ordering': ['name_jp']},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='writer',
            options={'ordering': ['name_reading']},
        ),
        migrations.AddField(
            model_name='musiccategory',
            name='order',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
