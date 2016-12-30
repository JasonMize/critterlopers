# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0002_auto_20161226_0057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='cast', blank=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comic',
            options={'ordering': ['-date_added']},
        ),
        migrations.AddField(
            model_name='comic',
            name='date_added',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now, blank=True, help_text='Posted on: '),
        ),
        migrations.AddField(
            model_name='cast',
            name='comic',
            field=models.ManyToManyField(null=True, blank=True, to='comic.Comic'),
        ),
    ]
