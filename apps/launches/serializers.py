from rest_framework import serializers


class ImageFormatSerializer(serializers.Serializer):
    """Serializer for image format data"""
    ext = serializers.CharField(max_length=10)
    url = serializers.URLField()
    hash = serializers.CharField(max_length=255)
    mime = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=255)
    path = serializers.CharField(max_length=500, required=False, allow_null=True)
    size = serializers.FloatField()
    width = serializers.IntegerField()
    height = serializers.IntegerField()


class ImageFormatsSerializer(serializers.Serializer):
    """Serializer for all image formats"""
    large = ImageFormatSerializer(required=False)
    small = ImageFormatSerializer(required=False) 
    medium = ImageFormatSerializer(required=False)
    thumbnail = ImageFormatSerializer(required=False)


class ImageSerializer(serializers.Serializer):
    """Serializer for image data"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    alternativeText = serializers.CharField(max_length=500, required=False, allow_null=True)
    caption = serializers.CharField(max_length=500, required=False, allow_null=True)
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    formats = ImageFormatsSerializer(required=False)
    hash = serializers.CharField(max_length=255)
    ext = serializers.CharField(max_length=10)
    mime = serializers.CharField(max_length=50)
    size = serializers.FloatField()
    url = serializers.URLField()
    previewUrl = serializers.URLField(required=False, allow_null=True)
    provider = serializers.CharField(max_length=100)
    provider_metadata = serializers.JSONField(required=False, allow_null=True)
    folderPath = serializers.CharField(max_length=500, required=False, allow_null=True)
    createdAt = serializers.DateTimeField()
    updatedAt = serializers.DateTimeField()
    documentId = serializers.CharField(max_length=255)
    locale = serializers.CharField(max_length=10, required=False, allow_null=True)
    publishedAt = serializers.DateTimeField()


class LaunchSerializer(serializers.Serializer):
    """Serializer for launch data"""
    id = serializers.IntegerField()
    documentId = serializers.CharField(max_length=255)
    correlationId = serializers.CharField(max_length=255, required=False, allow_null=True)
    endDate = serializers.DateField(required=False, allow_null=True)
    endTime = serializers.TimeField(required=False, allow_null=True)
    title = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(max_length=255, required=False, allow_null=True)
    quickDetail = serializers.CharField(max_length=500, required=False, allow_null=True)
    link = serializers.CharField(max_length=255)
    youtubeVideoId = serializers.CharField(max_length=255, required=False, allow_null=True)
    streamingVideoType = serializers.CharField(max_length=100, required=False, allow_null=True)
    callToAction = serializers.CharField(max_length=50)
    missionStatus = serializers.CharField(max_length=50)
    vehicle = serializers.CharField(max_length=100)
    returnSite = serializers.CharField(max_length=100, required=False, allow_null=True)
    launchSite = serializers.CharField(max_length=100)
    isOngoing = serializers.BooleanField()
    launchDate = serializers.DateField()
    launchTime = serializers.TimeField()
    missionType = serializers.CharField(max_length=100)
    directToCell = serializers.BooleanField()
    isLive = serializers.BooleanField()
    returnDateTime = serializers.DateTimeField(required=False, allow_null=True)
    showLaunchTimeInsteadOfWindow = serializers.CharField(max_length=10)
    imageDesktop = ImageSerializer(required=False, allow_null=True)
    imageMobile = ImageSerializer(required=False, allow_null=True)
    ongoingMissionImageDesktop = ImageSerializer(required=False, allow_null=True)
    ongoingMissionImageMobile = ImageSerializer(required=False, allow_null=True)
    videoDesktop = serializers.JSONField(required=False, allow_null=True)
    videoMobile = serializers.JSONField(required=False, allow_null=True)


class LaunchesResponseSerializer(serializers.Serializer):
    """Main serializer for launches API response"""
    total_launches = serializers.IntegerField()
    launches = LaunchSerializer(many=True)
    
    def to_representation(self, instance):
        """Create response structure from the raw launch data"""
        launches_data = instance if isinstance(instance, list) else []
        
        return {
            'total_launches': len(launches_data),
            'launches': launches_data
        }
