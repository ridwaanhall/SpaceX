from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_dragon_data
from .serializers import DragonRawDataSerializer
from .exceptions import APIError, DecryptionError, ValidationError
import logging

logger = logging.getLogger(__name__)


class DragonTrackingAPIView(APIView):
    """
    API view to get Dragon capsule tracking data.
    Returns the raw response from SpaceX API exactly as received, but validates with serializers.
    """
    
    def get(self, request):
        """
        GET /dragon/
        Returns Dragon capsule tracking data exactly as received from SpaceX API.
        """
        try:
            # Fetch data from the external SpaceX API
            raw_data = fetch_dragon_data()
            
            # Try to serialize the data, but don't fail if validation errors occur
            serializer = DragonRawDataSerializer(data=raw_data)
            
            if serializer.is_valid():
                return Response({
                    'success': True,
                    'message': 'Dragon tracking data retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                # If validation fails, return the raw data but log the errors
                logger.warning(f"Dragon serializer validation errors: {serializer.errors}")
                return Response({
                    'success': True,
                    'message': 'Dragon tracking data retrieved successfully',
                    'data': raw_data
                }, status=status.HTTP_200_OK)
        
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
            logger.error(f"Unexpected error in DragonTrackingAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'An unexpected error occurred. Please try again later.',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
