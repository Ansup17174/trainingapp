# Generated by Django 3.0.2 on 2020-02-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0002_auto_20200227_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='day',
            name='training_day',
            field=models.BooleanField(default=False),
        ),
    ]
