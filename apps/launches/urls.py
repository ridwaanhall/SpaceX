from django.urls import path
from . import views

app_name = 'launches'

urlpatterns = [
    path('', views.LaunchesAPIView.as_view(), name='spacex-launches'),
    path('health/', views.HealthCheckView.as_view(), name='health-check'),
    path('<str:link>/', views.LaunchDetailAPIView.as_view(), name='launch-detail'),
]
