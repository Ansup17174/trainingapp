# Generated by Django 3.0.2 on 2020-03-23 10:08

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0038_auto_20200323_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='weight',
            field=models.DecimalField(decimal_places=1, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='training',
            name='barbell_curl',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='barbell_ohp',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='barbell_row',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='bench_press',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='cable_crunch',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='calf_raises',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='chest_fly',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='chin_up',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='deadlift',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='dips',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='dumbell_ohp',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='dumbell_row',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='facepull',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='hammer_curl',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='hollow_body',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='incline_dumbell_curl',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='incline_press',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='lateral_raise',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='lunges',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='lying_dumbell_extension',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='pull_up',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='russian_twist',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
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
        migrations.AlterField(
            model_name='training',
            name='triceps_pressdown',
            field=models.DecimalField(decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='weighted_crunches',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='woodchoppers',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='average_weight',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
