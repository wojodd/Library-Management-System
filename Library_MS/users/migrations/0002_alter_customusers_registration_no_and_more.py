# Generated by Django 5.0 on 2023-12-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusers',
            name='Registration_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='contant_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='identification_no',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customusers',
            name='page_no',
            field=models.IntegerField(),
        ),
    ]
