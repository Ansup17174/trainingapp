from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.


class Week(models.Model):
    count = models.IntegerField()
    start_date = models.DateField(default=timezone.now)
    is_finished = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    average_weight = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return 'Tydzień {}'.format(self.count)


class Day(models.Model):
    class Meta:
        ordering = ('count',)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    weight = models.DecimalField(max_digits=5, decimal_places=1, null=True, validators=[MinValueValidator(Decimal('0.01'))])
    count = models.IntegerField()


class Training(models.Model):
    day = models.OneToOneField(Day, on_delete=models.CASCADE, primary_key=True)
    is_done = models.BooleanField(default=False)
    bench_press = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    barbell_ohp = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dips = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    chest_fly = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    lateral_raise = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    triceps_pressdown = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    deadlift = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    pull_up = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dumbell_row = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    barbell_curl = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    facepull = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    squat = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    stiff_legged_deadlift = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    lunges = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    calf_raises = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    incline_press = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    dumbell_ohp = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    chin_up = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    barbell_row = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    lying_dumbell_extension = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    incline_dumbell_curl = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hammer_curl = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    hollow_body = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    weighted_crunches = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    cable_crunch = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    woodchoppers = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    russian_twist = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    comment = models.CharField(blank=True, null=True, max_length=30)
