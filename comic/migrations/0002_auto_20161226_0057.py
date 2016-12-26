# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(null=True, blank=True, upload_to='images')),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='comics'),
        ),
    ]
