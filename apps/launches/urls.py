from django.urls import path
from . import views

app_name = 'launches'

urlpatterns = [
    path('', views.LaunchesAPIView.as_view(), name='spacex-launches'),
    path('<str:launch_id>/', views.LaunchDetailAPIView.as_view(), name='launch-detail'),
    path('health/', views.HealthCheckView.as_view(), name='health-check'),
]
