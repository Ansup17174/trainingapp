# Generated by Django 3.0.2 on 2020-03-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0026_auto_20200323_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='bench_press',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='deadlift',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='squat',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='stiff_legged_deadlift',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
    ]
