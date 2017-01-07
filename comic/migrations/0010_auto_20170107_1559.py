# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0009_auto_20170107_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='issue',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='page_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
