# Generated by Django 3.0.2 on 2020-02-27 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day',
            name='count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='barbell_ohp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='bench_press',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='chest_fly',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='dips',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='lateral_raise',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='fridaytraining',
            name='triceps_pressdown',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='barbell_curl',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='cable_crunch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='deadlift',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='dumbell_row',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='facepull',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='hollow_body',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='pull_up',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='russian_twist',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='weighted_crunches',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mondaytraining',
            name='woodchoppers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='barbell_row',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='chin_up',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='dumbell_ohp',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='facepull',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='hammer_curl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='incline_dumbell_curl',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='incline_press',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='lateral_raise',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='thirsdaytraining',
            name='lying_dumbell_extension',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='cable_crunch',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='calf_raises',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='hollow_body',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='lunges',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='russian_twist',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='squat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='stiff_legged_deadlift',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='weighted_crunches',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='wednesdaytraining',
            name='woodchoppers',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='count',
            field=models.IntegerField(),
        ),
    ]
