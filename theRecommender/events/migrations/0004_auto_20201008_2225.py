# Generated by Django 3.1.1 on 2020-10-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_remove_club_uni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='venue',
            field=models.CharField(max_length=100),
        ),
    ]