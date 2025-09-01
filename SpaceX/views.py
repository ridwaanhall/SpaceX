from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse


class APIRootView(APIView):
    """
    Root API view providing links to all available endpoints.
    """
    
    def get(self, request, format=None):
        return Response({
            'message': 'Welcome to SpaceX API',
            'version': '1.0',
            'endpoints': {
                'stats': request.build_absolute_uri(reverse('stats:spacex-stats')),
                'upcoming_launches': request.build_absolute_uri(reverse('upcoming:spacex-upcoming')),
                'launches': request.build_absolute_uri(reverse('launches:spacex-launches')),
                'health_checks': {
                    'stats': request.build_absolute_uri(reverse('stats:health-check')),
                    'upcoming': request.build_absolute_uri(reverse('upcoming:health-check')),
                    'launches': request.build_absolute_uri(reverse('launches:health-check')),
                }
            },
            'documentation': {
                'stats': 'Get SpaceX launch statistics including total launches, landings, and reflights',
                'upcoming_launches': 'Get upcoming SpaceX launches with detailed mission information',
                'launches': 'Get past SpaceX launches with mission details and status'
            }
        }, status=status.HTTP_200_OK)
