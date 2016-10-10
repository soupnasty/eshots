# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first', models.CharField(max_length=25)),
                ('last', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
