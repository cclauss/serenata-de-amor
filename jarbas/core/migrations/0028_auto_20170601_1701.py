# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_translate_verbose_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreimbursement',
            name='history_type',
            field=models.CharField(choices=[('+', 'Criado'), ('~', 'Modificado'), ('-', 'Excluído')], max_length=1),
        ),
    ]
