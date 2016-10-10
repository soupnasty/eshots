# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('course', models.CharField(max_length=1, choices=[('1', 'Math 101'), ('2', 'English 101'), ('3', 'Science 101'), ('4', 'Social Studies 101'), ('5', 'Health 101'), ('6', 'Chemistry 101'), ('7', 'English 201'), ('8', 'Math 201')], null=True)),
                ('grade', models.DecimalField(decimal_places=1, max_digits=2)),
                ('student', models.ForeignKey(related_name='classes', to='students.Student')),
            ],
        ),
    ]
