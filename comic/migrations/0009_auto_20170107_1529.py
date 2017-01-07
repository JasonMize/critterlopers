# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0008_comic_sort_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comic',
            options={'ordering': ['-sort_number', '-date_added']},
        ),
    ]
