from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_spacex_data
from .serializers import SpaceXStatsSerializer
from .exceptions import APIError, DecryptionError, ValidationError
import logging

logger = logging.getLogger(__name__)


class SpaceXStatsAPIView(APIView):
    """
    API view to get SpaceX launch statistics.
    Fetches data from encrypted SpaceX API and returns structured response.
    """
    
    def get(self, request):
        """
        GET /stats/
        Returns SpaceX launch statistics and data.
        """
        try:
            # Fetch data from the external SpaceX API
            raw_data = fetch_spacex_data()
            
            # Serialize the data
            serializer = SpaceXStatsSerializer(data=raw_data)
            
            if serializer.is_valid():
                return Response({
                    'success': True,
                    'message': 'SpaceX statistics retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                # Log serializer errors but don't expose them to the user
                logger.warning(f"Serializer validation errors: {serializer.errors}")
                return Response({
                    'success': False,
                    'message': 'Invalid data format received from SpaceX API',
                    'data': None
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except DecryptionError as e:
            return Response({
                'success': False,
                'message': str(e),
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except ValidationError as e:
            return Response({
                'success': False,
                'message': str(e),
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except APIError as e:
            return Response({
                'success': False,
                'message': str(e),
                'data': None
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            logger.error(f"Unexpected error in SpaceXStatsAPIView: {str(e)}")
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
            'message': 'SpaceX API is running'
        }, status=status.HTTP_200_OK)
