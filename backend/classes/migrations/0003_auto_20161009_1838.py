# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20161009_1833'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'ordering': ['student', 'course']},
        ),
        migrations.AlterUniqueTogether(
            name='class',
            unique_together=set([('course', 'student')]),
        ),
    ]
