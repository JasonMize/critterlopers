# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0005_auto_20161230_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='description',
            field=models.CharField(max_length=400, blank=True, null=True),
        ),
    ]
