# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0003_auto_20161230_0331'),
    ]

    operations = [
        migrations.AddField(
            model_name='comic',
            name='page_number',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='cast',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comic',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='headerimage',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
