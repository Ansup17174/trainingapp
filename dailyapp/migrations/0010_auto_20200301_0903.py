# Generated by Django 3.0.2 on 2020-03-01 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0009_remove_day_training_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='finished',
            field=models.TextField(default='Nie'),
        ),
    ]