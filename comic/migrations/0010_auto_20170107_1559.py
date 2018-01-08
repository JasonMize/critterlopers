# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comic', '0009_auto_20170107_1529'),
    ]
    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, blank=True, max_length=200)),
                ('image', models.ImageField(null=True, blank=True, upload_to='issues')),
                ('issue_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='comic',
            name='issue',
            field=models.ForeignKey(null=True, to='comic.Issue', blank=True),
        ),
    ]
