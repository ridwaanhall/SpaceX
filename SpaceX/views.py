from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.conf import settings


class APIRootView(APIView):
    """
    Root API view providing links to all available endpoints.
    """
    
    def get(self, request, format=None):
        # Check if full API is available
        if not settings.IS_AVAILABLE:
            return Response({
                'message': 'SpaceX API - Limited Access',
                'version': settings.VERSION,
                'status': 'limited',
                'reason': 'API access is currently limited due to high traffic',
                'available_endpoints': {
                    'root': {
                        'url': request.build_absolute_uri('/'),
                        'description': 'This root endpoint (current page)'
                    }
                },
                'notice': 'Most API endpoints are temporarily unavailable. Please try again later.',
                'contact': 'For urgent access requirements, please contact the administrator.',
                'limited_apps': ['Only root endpoint available']
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        # Full API is available
        return Response({
            'message': 'Welcome to SpaceX API',
            'version': settings.VERSION,
            'status': 'operational',
            'endpoints': {
                'stats': {
                    'url': request.build_absolute_uri(reverse('stats:spacex-stats')),
                    'description': 'Get SpaceX launch statistics including total launches, landings, and reflights'
                },
                'upcoming_launches': {
                    'list': request.build_absolute_uri(reverse('upcoming:spacex-upcoming')),
                    'stats': request.build_absolute_uri(reverse('upcoming:upcoming-stats')),
                    'description': 'Get upcoming SpaceX launches with detailed mission information and stats'
                },
                'launches': {
                    'list': request.build_absolute_uri(reverse('launches:spacex-launches')),
                    'detail': request.build_absolute_uri('/launches/{link}/'),
                    'description': 'Get past SpaceX launches with mission details. Use the "link" field from launch data to get detailed information'
                },
                'dragon': {
                    'url': request.build_absolute_uri(reverse('dragon:dragon-tracking')),
                    'description': 'Get real-time Dragon capsule GPS tracking and telemetry data (returns raw SpaceX API response)'
                },
                'health_checks': {
                    'stats': request.build_absolute_uri(reverse('stats:health-check')),
                    'upcoming': request.build_absolute_uri(reverse('upcoming:health-check')),
                    'launches': request.build_absolute_uri(reverse('launches:health-check')),
                }
            },
            'usage_examples': {
                'get_stats': request.build_absolute_uri(reverse('stats:spacex-stats')),
                'get_upcoming_launches': request.build_absolute_uri(reverse('upcoming:spacex-upcoming')),
                'get_upcoming_stats': request.build_absolute_uri(reverse('upcoming:upcoming-stats')),
                'get_all_launches': request.build_absolute_uri(reverse('launches:spacex-launches')),
                'get_launch_detail': 'Use /launches/{link}/ where {link} is from the launch data (e.g., /launches/crew11/)',
                'get_dragon_tracking': request.build_absolute_uri(reverse('dragon:dragon-tracking'))
            },
            'available_apps': ['stats', 'upcoming', 'launches', 'dragon'],
            'note': 'All endpoints return JSON data. The launches detail endpoint requires a "link" parameter from the launches list. Dragon endpoint returns raw SpaceX API response with GPS tracking data.'
        }, status=status.HTTP_200_OK)
