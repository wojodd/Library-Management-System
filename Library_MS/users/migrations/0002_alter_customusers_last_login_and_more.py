# Generated by Django 4.2.8 on 2023-12-28 06:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='last_login',
            field=models.CharField(default=datetime.date(1, 1, 1), max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customusers',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]
