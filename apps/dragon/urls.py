from django.urls import path
from .views import DragonTrackingAPIView

app_name = 'dragon'

urlpatterns = [
    # Dragon GPS tracking data - returns raw SpaceX API response
    path('', DragonTrackingAPIView.as_view(), name='dragon-tracking'),
]
