from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_launches_data
from .serializers import LaunchesResponseSerializer, LaunchSerializer
import logging

logger = logging.getLogger(__name__)


class LaunchesAPIView(APIView):
    """
    API view to get SpaceX launches data.
    Fetches data from encrypted SpaceX API and returns structured response.
    """
    
    def get(self, request):
        """
        GET /launches/
        Returns SpaceX launches data.
        """
        try:
            # Fetch data from the external SpaceX API
            raw_data = fetch_launches_data()
            
            # Serialize the data
            serializer = LaunchesResponseSerializer(raw_data)
            
            return Response({
                'success': True,
                'message': 'SpaceX launches data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in LaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve SpaceX launches data: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LaunchDetailAPIView(APIView):
    """
    API view to get a specific launch by ID or link.
    """
    
    def get(self, request, launch_id=None):
        """
        GET /launches/{launch_id}/
        Returns specific SpaceX launch data.
        """
        try:
            # Fetch all launches data
            raw_data = fetch_launches_data()
            
            # Find specific launch
            launch = None
            for item in raw_data:
                if str(item.get('id')) == str(launch_id) or item.get('link') == str(launch_id):
                    launch = item
                    break
            
            if not launch:
                return Response({
                    'success': False,
                    'message': f'Launch with ID/link "{launch_id}" not found',
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Serialize the launch data
            serializer = LaunchSerializer(data=launch)
            
            if serializer.is_valid():
                return Response({
                    'success': True,
                    'message': 'Launch data retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': False,
                    'message': 'Invalid launch data format',
                    'errors': serializer.errors,
                    'data': launch
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
        except Exception as e:
            logger.error(f"Error in LaunchDetailAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve launch data: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HealthCheckView(APIView):
    """
    Simple health check endpoint
    """
    
    def get(self, request):
        return Response({
            'status': 'healthy',
            'message': 'Launches API is running'
        }, status=status.HTTP_200_OK)
