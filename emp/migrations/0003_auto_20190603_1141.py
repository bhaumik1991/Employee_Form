# Generated by Django 2.1 on 2019-06-03 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_auto_20190601_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
