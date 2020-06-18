# Generated by Django 3.0.2 on 2020-03-04 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dailyapp', '0014_auto_20200302_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('day', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dailyapp.Day')),
                ('bench_press', models.PositiveIntegerField(blank=True, null=True)),
                ('barbell_ohp', models.PositiveIntegerField(blank=True, null=True)),
                ('dips', models.PositiveIntegerField(blank=True, null=True)),
                ('chest_fly', models.PositiveIntegerField(blank=True, null=True)),
                ('lateral_raise', models.PositiveIntegerField(blank=True, null=True)),
                ('triceps_pressdown', models.PositiveIntegerField(blank=True, null=True)),
                ('deadlift', models.PositiveIntegerField(blank=True, null=True)),
                ('pull_up', models.PositiveIntegerField(blank=True, null=True)),
                ('dumbell_row', models.PositiveIntegerField(blank=True, null=True)),
                ('barbell_curl', models.PositiveIntegerField(blank=True, null=True)),
                ('facepull', models.PositiveIntegerField(blank=True, null=True)),
                ('squat', models.PositiveIntegerField(blank=True, null=True)),
                ('stiff_legged_deadlift', models.IntegerField(blank=True, null=True)),
                ('lunges', models.PositiveIntegerField(blank=True, null=True)),
                ('calf_raises', models.PositiveIntegerField(blank=True, null=True)),
                ('incline_press', models.PositiveIntegerField(blank=True, null=True)),
                ('dumbell_ohp', models.PositiveIntegerField(blank=True, null=True)),
                ('chin_up', models.PositiveIntegerField(blank=True, null=True)),
                ('barbell_row', models.PositiveIntegerField(blank=True, null=True)),
                ('lying_dumbell_extension', models.PositiveIntegerField(blank=True, null=True)),
                ('incline_dumbell_curl', models.PositiveIntegerField(blank=True, null=True)),
                ('hammer_curl', models.PositiveIntegerField(blank=True, null=True)),
                ('hollow_body', models.IntegerField(blank=True, null=True)),
                ('weighted_crunches', models.IntegerField(blank=True, null=True)),
                ('cable_crunch', models.IntegerField(blank=True, null=True)),
                ('woodchoppers', models.IntegerField(blank=True, null=True)),
                ('russian_twist', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sundaytraining',
            name='day',
        ),
        migrations.RemoveField(
            model_name='thirsdaytraining',
            name='day',
        ),
        migrations.RemoveField(
            model_name='wednesdaytraining',
            name='day',
        ),
        migrations.DeleteModel(
            name='MondayTraining',
        ),
        migrations.DeleteModel(
            name='SundayTraining',
        ),
        migrations.DeleteModel(
            name='ThirsdayTraining',
        ),
        migrations.DeleteModel(
            name='WednesdayTraining',
        ),
    ]