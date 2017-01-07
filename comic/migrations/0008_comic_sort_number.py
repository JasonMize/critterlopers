# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0007_auto_20161231_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='sort_number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
