from django.urls import path
from . import views

app_name = 'dailyapp'

urlpatterns = [
    path('', views.MainView.as_view(), name="main_view"),
    path('day/<int:pk>/', views.DayView.as_view(), name='day_view'),
    path('history/', views.WeekHistory.as_view(), name='week_history'),
    path('stats/', views.StatsView.as_view(), name='stats_view'),
]