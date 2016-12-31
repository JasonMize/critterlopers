# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0006_cast_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cast',
            name='comic',
        ),
        migrations.AddField(
            model_name='comic',
            name='cast_members',
            field=models.ManyToManyField(to='comic.Cast', blank=True, related_name='comics'),
        ),
    ]
