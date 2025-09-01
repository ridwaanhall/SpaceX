from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .utils import fetch_upcoming_launches
from .serializers import UpcomingLaunchesResponseSerializer, UpcomingLaunchSerializer
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
            
            # Add validation errors if any (but still return successful response)
            if launch_errors:
                response_data['validation_warnings'] = {
                    'message': f'{len(launch_errors)} launches had validation issues',
                    'errors': launch_errors[:5]  # Limit to first 5 errors
                }
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error in UpcomingLaunchesAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve upcoming launches: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpcomingLaunchDetailAPIView(APIView):
    """
    API view to get a specific upcoming launch by ID.
    """
    
    def get(self, request, launch_id):
        """
        GET /upcoming/{launch_id}/
        Returns specific launch details by ID.
        """
        try:
            # Fetch all launches data
            raw_data = fetch_upcoming_launches()
            
            # Find the specific launch
            launch_data = None
            for launch in raw_data:
                if launch.get('id') == launch_id:
                    launch_data = launch
                    break
            
            if not launch_data:
                return Response({
                    'success': False,
                    'message': f'Launch with ID {launch_id} not found',
                    'data': None
                }, status=status.HTTP_404_NOT_FOUND)
            
            # Serialize the launch data
            serializer = UpcomingLaunchSerializer(data=launch_data)
            
            if serializer.is_valid():
                return Response({
                    'success': True,
                    'message': 'Launch details retrieved successfully',
                    'data': serializer.validated_data
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'success': False,
                    'message': 'Invalid launch data format',
                    'errors': serializer.errors,
                    'raw_data': launch_data
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        except Exception as e:
            logger.error(f"Error in UpcomingLaunchDetailAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve launch details: {str(e)}',
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
            
        except Exception as e:
            logger.error(f"Error in UpcomingStatsAPIView: {str(e)}")
            return Response({
                'success': False,
                'message': f'Failed to retrieve upcoming launches statistics: {str(e)}',
                'data': None
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
