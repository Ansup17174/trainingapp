# Generated by Django 3.0.2 on 2020-03-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0037_auto_20200323_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='average_weight',
            field=models.FloatField(null=True),
        ),
    ]
