# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='student',
            field=models.ForeignKey(related_name='classes', null=True, to='students.Student', blank=True),
        ),
    ]
