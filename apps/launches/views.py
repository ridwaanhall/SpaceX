from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_launches_data, fetch_launch_detail
from .serializers import LaunchesResponseSerializer, LaunchSerializer, LaunchDetailSerializer
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
    API view to get detailed SpaceX launch information.
    Fetches detailed data for a specific launch using the link parameter.
    """
    
    def get(self, request, link):
        """
        GET /launches/{link}/
        Returns detailed SpaceX launch information for the specified link.
        """
        try:
            # Fetch detailed data from the external SpaceX API
            raw_data = fetch_launch_detail(link)
            
            # Try to serialize the data, but don't fail if validation errors occur
            serializer = LaunchDetailSerializer(data=raw_data)
            
            if serializer.is_valid():
                return Response({
                    'success': True,
                    'message': f'Launch detail for {link} retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                # If validation fails, return the raw data but log the errors
                logger.warning(f"Serializer validation errors for {link}: {serializer.errors}")
                return Response({
                    'success': True,
                    'message': f'Launch detail for {link} retrieved successfully (with validation warnings)',
                    'data': raw_data,
                    'validation_warnings': serializer.errors
                }, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in LaunchDetailAPIView for {link}: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve launch detail for {link}: {str(e)}',
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
