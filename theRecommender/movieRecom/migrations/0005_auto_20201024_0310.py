# Generated by Django 3.1.1 on 2020-10-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieRecom', '0004_auto_20201024_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='movieid',
            field=models.IntegerField(),
        ),
    ]
