from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import fetch_upcoming_launches
from .serializers import UpcomingLaunchesResponseSerializer, UpcomingLaunchSerializer
from .exceptions import APIError, DecryptionError, ValidationError
import logging

logger = logging.getLogger(__name__)


class UpcomingLaunchesAPIView(APIView):
    """
    API view to get upcoming SpaceX launches.
    Fetches data from encrypted SpaceX API and returns structured response.
    """
    
    def get(self, request):
        """
        GET /upcoming/
        Returns upcoming SpaceX launches data with statistics.
        """
        try:
            # Fetch data from the external SpaceX API
            raw_data = fetch_upcoming_launches()
            
            # Validate individual launches
            launch_errors = []
            validated_launches = []
            
            for idx, launch_data in enumerate(raw_data):
                launch_serializer = UpcomingLaunchSerializer(data=launch_data)
                if launch_serializer.is_valid():
                    validated_launches.append(launch_serializer.validated_data)
                else:
                    launch_errors.append({
                        'launch_index': idx,
                        'errors': launch_serializer.errors
                    })
            
            # Create response with statistics
            response_serializer = UpcomingLaunchesResponseSerializer(validated_launches)
            
            response_data = {
                'success': True,
                'message': 'Upcoming launches retrieved successfully',
                'data': response_serializer.data
            }
            
            # Log validation errors but don't expose them to the user
            if launch_errors:
                logger.warning(f'{len(launch_errors)} launches had validation issues')
            
            return Response(response_data, status=status.HTTP_200_OK)
        
        except DecryptionError as e:
            logger.error(f"Decryption error in UpcomingLaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'Data decryption failed. Please try again later.',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except ValidationError as e:
            logger.error(f"Validation error in UpcomingLaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'Invalid request data provided.',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except APIError as e:
            logger.error(f"API error in UpcomingLaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'External service temporarily unavailable. Please try again later.',
                'data': None
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            logger.error(f"Unexpected error in UpcomingLaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'An unexpected error occurred. Please try again later.',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class UpcomingStatsAPIView(APIView):
    """
    API view to get statistics about upcoming launches.
    """
    
    def get(self, request):
        """
        GET /upcoming/stats/
        Returns statistics about upcoming launches.
        """
        try:
            # Fetch data from the external SpaceX API
            raw_data = fetch_upcoming_launches()
            
            # Calculate statistics
            total_launches = len(raw_data)
            upcoming_launches = len([launch for launch in raw_data if launch.get('missionStatus') == 'upcoming'])
            starlink_missions = len([launch for launch in raw_data if launch.get('missionType') == 'starlink'])
            live_launches = len([launch for launch in raw_data if launch.get('isLive') == True])
            ongoing_launches = len([launch for launch in raw_data if launch.get('isOngoing') == True])
            
            # Group by vehicle
            vehicles = {}
            for launch in raw_data:
                vehicle = launch.get('vehicle', 'Unknown')
                vehicles[vehicle] = vehicles.get(vehicle, 0) + 1
            
            # Group by launch site
            launch_sites = {}
            for launch in raw_data:
                site = launch.get('launchSite', 'Unknown')
                launch_sites[site] = launch_sites.get(site, 0) + 1
            
            return Response({
                'success': True,
                'message': 'Upcoming launches statistics retrieved successfully',
                'data': {
                    'total_launches': total_launches,
                    'upcoming_launches': upcoming_launches,
                    'starlink_missions': starlink_missions,
                    'live_launches': live_launches,
                    'ongoing_launches': ongoing_launches,
                    'vehicles': vehicles,
                    'launch_sites': launch_sites
                }
            }, status=status.HTTP_200_OK)
        
        except DecryptionError as e:
            logger.error(f"Decryption error in UpcomingStatsAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'Data decryption failed. Please try again later.',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        except ValidationError as e:
            logger.error(f"Validation error in UpcomingStatsAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'Invalid request data provided.',
                'data': None
            }, status=status.HTTP_400_BAD_REQUEST)
        
        except APIError as e:
            logger.error(f"API error in UpcomingStatsAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'External service temporarily unavailable. Please try again later.',
                'data': None
            }, status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            logger.error(f"Unexpected error in UpcomingStatsAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': 'An unexpected error occurred. Please try again later.',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HealthCheckView(APIView):
    """
    Simple health check endpoint for upcoming launches API
    """
    
    def get(self, request):
        return Response({
            'status': 'healthy',
            'message': 'Upcoming Launches API is running'
        }, status=status.HTTP_200_OK)
