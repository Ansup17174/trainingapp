# Generated by Django 3.0.2 on 2020-03-01 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0011_auto_20200301_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='valid',
            field=models.BooleanField(default=False),
        ),
    ]