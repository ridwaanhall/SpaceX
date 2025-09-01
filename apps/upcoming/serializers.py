from rest_framework import serializers


class ImageFormatSerializer(serializers.Serializer):
    """Serializer for image format (large, medium, small, thumbnail)"""
    ext = serializers.CharField(max_length=10)
    url = serializers.URLField()
    hash = serializers.CharField(max_length=255)
    mime = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=255, required=False, allow_null=True)
    size = serializers.FloatField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()


class ImageFormatsSerializer(serializers.Serializer):
    """Serializer for image formats collection"""
    large = ImageFormatSerializer(required=False)
    small = ImageFormatSerializer(required=False)
    medium = ImageFormatSerializer(required=False)
    thumbnail = ImageFormatSerializer(required=False)


class LaunchImageSerializer(serializers.Serializer):
    """Serializer for launch images (desktop/mobile)"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    alternativeText = serializers.CharField(max_length=255, required=False, allow_null=True)
    caption = serializers.CharField(max_length=255, required=False, allow_null=True)
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    formats = ImageFormatsSerializer(required=False)
    hash = serializers.CharField(max_length=255)
    ext = serializers.CharField(max_length=10)
    mime = serializers.CharField(max_length=50)
    size = serializers.FloatField()
    url = serializers.URLField()
    previewUrl = serializers.URLField(required=False, allow_null=True)
    provider = serializers.CharField(max_length=100, required=False, allow_null=True)
    provider_metadata = serializers.JSONField(required=False, allow_null=True)
    folderPath = serializers.CharField(max_length=255, required=False, allow_null=True)
    createdAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    documentId = serializers.CharField(max_length=255)
    locale = serializers.CharField(max_length=10, required=False, allow_null=True)
    publishedAt = serializers.DateTimeField(required=False, allow_null=True)


class UpcomingLaunchSerializer(serializers.Serializer):
    """Serializer for individual upcoming launch data"""
    id = serializers.IntegerField()
    documentId = serializers.CharField(max_length=255)
    correlationId = serializers.CharField(max_length=255, required=False, allow_null=True)
    endDate = serializers.DateField(required=False, allow_null=True)
    endTime = serializers.TimeField(required=False, allow_null=True)
    title = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(max_length=255, required=False, allow_null=True)
    quickDetail = serializers.CharField(max_length=500, required=False, allow_null=True)
    link = serializers.CharField(max_length=255, required=False, allow_null=True)
    youtubeVideoId = serializers.CharField(max_length=255, required=False, allow_null=True)
    streamingVideoType = serializers.CharField(max_length=100, required=False, allow_null=True)
    callToAction = serializers.CharField(max_length=100, required=False, allow_null=True)
    missionStatus = serializers.CharField(max_length=50)
    vehicle = serializers.CharField(max_length=100, required=False, allow_null=True)
    returnSite = serializers.CharField(max_length=255, required=False, allow_null=True)
    launchSite = serializers.CharField(max_length=255, required=False, allow_null=True)
    isOngoing = serializers.BooleanField(default=False)
    launchDate = serializers.DateField(required=False, allow_null=True)
    launchTime = serializers.TimeField(required=False, allow_null=True)
    missionType = serializers.CharField(max_length=100, required=False, allow_null=True)
    directToCell = serializers.BooleanField(default=False)
    isLive = serializers.BooleanField(default=False)
    returnDateTime = serializers.DateTimeField(required=False, allow_null=True)
    showLaunchTimeInsteadOfWindow = serializers.CharField(max_length=10, required=False, allow_null=True)
    
    # Image fields
    imageDesktop = LaunchImageSerializer(required=False, allow_null=True)
    imageMobile = LaunchImageSerializer(required=False, allow_null=True)
    ongoingMissionImageDesktop = LaunchImageSerializer(required=False, allow_null=True)
    ongoingMissionImageMobile = LaunchImageSerializer(required=False, allow_null=True)
    videoDesktop = serializers.JSONField(required=False, allow_null=True)
    videoMobile = serializers.JSONField(required=False, allow_null=True)


class UpcomingLaunchesResponseSerializer(serializers.Serializer):
    """Main response serializer for upcoming launches"""
    total_count = serializers.IntegerField()
    upcoming_count = serializers.IntegerField()
    starlink_count = serializers.IntegerField()
    launches = UpcomingLaunchSerializer(many=True)
    
    def to_representation(self, instance):
        """Create summary stats from the raw launch data"""
        launches_data = instance if isinstance(instance, list) else []
        
        # Calculate stats
        total_count = len(launches_data)
        upcoming_count = len([launch for launch in launches_data if launch.get('missionStatus') == 'upcoming'])
        starlink_count = len([launch for launch in launches_data if launch.get('missionType') == 'starlink'])
        
        return {
            'total_count': total_count,
            'upcoming_count': upcoming_count,
            'starlink_count': starlink_count,
            'launches': launches_data
        }
