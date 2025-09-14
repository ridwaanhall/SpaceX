from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_launches_data, fetch_launch_detail, sort_launches_by_datetime, APIError, NotFoundError, ValidationError
from .serializers import LaunchesResponseSerializer, LaunchDetailSerializer
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
        Supports query parameter: sort=datetime (sorts by launch date and time, latest first)
        """
        try:
            # Get the sort parameter from query string
            sort_param = request.GET.get('sort', None)
            
            # Fetch data from the external SpaceX API
            raw_data = fetch_launches_data()
            
            # Extract launches from the response data
            launches_list = []
            if isinstance(raw_data, dict):
                # If the response has a 'data' key with launches inside
                if 'data' in raw_data and 'launches' in raw_data['data']:
                    launches_list = raw_data['data']['launches']
                # If the response has launches directly
                elif 'launches' in raw_data:
                    launches_list = raw_data['launches']
                # If the response is just a list of launches
                elif isinstance(raw_data.get('data'), list):
                    launches_list = raw_data['data']
            elif isinstance(raw_data, list):
                # If the response is directly a list of launches
                launches_list = raw_data
            
            # Apply sorting if requested
            if sort_param == 'datetime' and launches_list:
                launches_list = sort_launches_by_datetime(launches_list)
            
            # Serialize the data
            serializer = LaunchesResponseSerializer(launches_list)
            
            return Response({
                'success': True,
                'message': 'SpaceX launches data retrieved successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        
        except APIError as e:
            logger.error(f"API error in LaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'External service temporarily unavailable. Please try again later.',
                'data': None
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        
        except NotFoundError as e:
            logger.error(f"Not found error in LaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'The requested resource was not found.',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)
            
        except Exception as e:
            logger.error(f"Unexpected error in LaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'An unexpected error occurred. Please try again later.',
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
                    'message': f'Launch details retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                # If validation fails, return the raw data but log the errors
                logger.warning(f"Serializer validation errors for {link}: {serializer.errors}")
                return Response({
                    'success': True,
                    'message': 'Launch details retrieved successfully',
                    'data': raw_data
                }, status=status.HTTP_200_OK)
        
        except ValidationError as e:
            logger.error(f"Validation error in LaunchDetailAPIView for {link}: {str(e)}")
            return Response({
                'success': False,
                'message': 'Invalid request data provided.',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except NotFoundError as e:
            logger.error(f"Not found error in LaunchDetailAPIView for {link}: {str(e)}")
            return Response({
                'success': False,
                'message': 'The requested launch was not found.',
                'data': None
            }, status=status.HTTP_404_NOT_FOUND)
        
        except APIError as e:
            logger.error(f"API error in LaunchDetailAPIView for {link}: {str(e)}")
            return Response({
                'success': False,
                'message': 'External service temporarily unavailable. Please try again later.',
                'data': None
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            logger.error(f"Unexpected error in LaunchDetailAPIView for {link}: {str(e)}")
            return Response({
                'success': False,
                'message': 'An unexpected error occurred. Please try again later.',
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
