# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0004_auto_20161230_0338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='comic',
            field=models.ManyToManyField(to='comic.Comic', blank=True),
        ),
    ]
