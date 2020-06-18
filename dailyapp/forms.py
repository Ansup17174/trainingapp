from django import forms
from .models import *


class WeightForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ('weight',)


class SundayTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('bench_press', 'barbell_ohp', 'dips',
                  'chest_fly', 'lateral_raise', 'triceps_pressdown')


class MondayTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('deadlift', 'pull_up', 'dumbell_row', 'barbell_curl',
                  'facepull', 'hollow_body', 'weighted_crunches',
                  'cable_crunch', 'woodchoppers', 'russian_twist')


class WednesdayTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('squat', 'stiff_legged_deadlift', 'lunges', 'calf_raises', 'hollow_body', 'weighted_crunches',
                  'cable_crunch', 'woodchoppers', 'russian_twist')


class ThirsdayTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('incline_press', 'dumbell_ohp', 'chin_up', 'barbell_row',
                  'lying_dumbell_extension', 'incline_dumbell_curl',
                  'hammer_curl', 'lateral_raise', 'facepull')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ('comment',)