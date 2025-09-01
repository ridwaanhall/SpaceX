from django.urls import path
from . import views

app_name = 'stats'

urlpatterns = [
    path('', views.SpaceXStatsAPIView.as_view(), name='spacex-stats'),
    path('health/', views.HealthCheckView.as_view(), name='health-check'),
]
