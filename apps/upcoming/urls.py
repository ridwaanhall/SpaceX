from django.urls import path
from . import views

app_name = 'upcoming'

urlpatterns = [
    path('', views.UpcomingLaunchesAPIView.as_view(), name='spacex-upcoming'),
    path('stats/', views.UpcomingStatsAPIView.as_view(), name='upcoming-stats'),
    path('health/', views.HealthCheckView.as_view(), name='health-check'),
]
