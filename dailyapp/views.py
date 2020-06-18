from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
import json
from decimal import Decimal

# Create your views here.


class MainView(View):

    def get(self, request):
        try:
            week = Week.objects.all().order_by('-count')[0]
        except IndexError:
            week = Week.objects.create(count=1)
            for num in range(1, 8):
                day = Day.objects.create(week=week, count=num, date=timezone.now()+timezone.timedelta(days=num-1))
                if num == 2 or num == 3 or num == 5 or num == 6:
                    day.training = Training.objects.create(day=day)
                day.save()
        days = week.day_set.order_by('date')
        valid_status = True
        for day in days:
            if day.count == 2 or day.count == 3 or day.count == 5 or day.count == 6:
                if not day.training.is_done:
                    valid_status = False
            if not day.weight:
                valid_status = False
        week.is_valid = valid_status
        week.save()
        context = {'week': week, 'days': days}
        return render(request, 'dailyapp/week_list.html', context)

    def post(self, request):
        last_week = Week.objects.all().order_by('-count')[0]
        days = last_week.day_set.order_by('date')
        total_weight = 0
        for day in days:
            total_weight += day.weight
        last_week.average_weight = total_weight / 7
        last_week.is_finished = True
        last_week.save()
        last_day = last_week.day_set.order_by('-date')[0]
        current_week = Week.objects.create(count=last_week.count + 1,
                                           start_date=last_week.start_date + timezone.timedelta(days=7))
        for num in range(1, 8):
            day = Day.objects.create(week=current_week, count=num, date=last_day.date+timezone.timedelta(days=num))
            if num == 2 or num == 3 or num == 5 or num == 6:
                day.training = Training.objects.create(day=day)
            day.save()
        return HttpResponseRedirect(reverse('dailyapp:main_view'))


class DayView(View):

    def get(self, request, pk, *args, **kwargs):
        day = get_object_or_404(Day, pk=pk)
        training_forms = (None, SundayTrainingForm, MondayTrainingForm,
                          None, WednesdayTrainingForm, ThirsdayTrainingForm, None,
        )
        training_form = training_forms[day.count-1]
        comment_form = None
        if training_form:
            training_form = training_form()
            comment_form = CommentForm()
        weight_form = WeightForm()
        context = {'day': day, 'training_form': training_form, 'weight_form': weight_form,
                   'comment_form': comment_form}
        return render(request, 'dailyapp/day_info.html', context)

    def post(self, request, pk, *args, **kwargs):
        day = get_object_or_404(Day, pk=pk)
        training_forms = (
        None, SundayTrainingForm, MondayTrainingForm, None, WednesdayTrainingForm, ThirsdayTrainingForm, None)
        training_form = training_forms[day.count-1]
        if training_form:
            training_form = training_form(request.POST)
            if training_form.is_valid():
                training = training_form.save(commit=False)
                training.day = day
                training.is_done = True
                training.save()
                return HttpResponseRedirect(reverse('dailyapp:main_view'))
        weight_form = WeightForm(request.POST, instance=day)
        if weight_form.is_valid():
            weight = weight_form.save(commit=False)
            weight.week = day.week
            weight.day = day
            weight.count = day.count
            weight.save()
            return HttpResponseRedirect(reverse('dailyapp:main_view'))
        comment_form = CommentForm(request.POST, instance=day.training)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.training = day.training
            comment.save()
            return HttpResponseRedirect(reverse('dailyapp:main_view'))
        return HttpResponseRedirect(reverse('dailyapp:day_view', args=(pk,)))

class WeekHistory(View):

    def get(self, request):
        weeks = Week.objects.all().order_by('pk').filter(is_finished=True)
        context = {'weeks': weeks}
        return render(request, 'dailyapp/week_history.html', context)


class StatsView(View):

    def get(self, request):
        weeks = Week.objects.filter(is_finished=True).order_by('pk')
        weight_data = json.dumps({str(week.start_date): float(week.average_weight) for week in weeks})
        context = {'weight_data': weight_data}
        return render(request, 'dailyapp/stats.html', context)

    def post(self, request):
        weeks = Week.objects.filter(is_finished=True).order_by('pk')
        weight_data = json.dumps({str(week.start_date): float(week.average_weight) for week in weeks})
        exercise = request.POST['exercises']
        trainings = Training.objects.filter(is_done=True).order_by('day_id')
        exercise_data = {str(training.day.date): (float(getattr(training, exercise)), getattr(training, 'comment'))
                         for training in trainings if getattr(training, exercise)}
        exercise = exercise.split('_')
        exercise = ' '.join(exercise).capitalize()
        context = {'weight_data': weight_data, 'exercise': exercise, 'exercise_data': json.dumps(exercise_data)}
        return render(request, 'dailyapp/stats.html', context)

# collapsible
