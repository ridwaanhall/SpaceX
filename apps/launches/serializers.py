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
    sizeInBytes = serializers.IntegerField(required=False)


class ImageFormatsSerializer(serializers.Serializer):
    """Serializer for all image formats"""
    large = ImageFormatSerializer(required=False, allow_null=True)
    small = ImageFormatSerializer(required=False, allow_null=True) 
    medium = ImageFormatSerializer(required=False, allow_null=True)
    thumbnail = ImageFormatSerializer(required=False, allow_null=True)


class ImageSerializer(serializers.Serializer):
    """Serializer for image data"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    alternativeText = serializers.CharField(max_length=500, required=False, allow_null=True)
    caption = serializers.CharField(max_length=500, required=False, allow_null=True)
    width = serializers.IntegerField()
    height = serializers.IntegerField()
    formats = ImageFormatsSerializer(required=False, allow_null=True)
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


class TimelineEntrySerializer(serializers.Serializer):
    """Serializer for timeline entry data"""
    id = serializers.IntegerField()
    time = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=500)


class TimelineSerializer(serializers.Serializer):
    """Serializer for timeline data"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255, required=False)
    title = serializers.CharField(max_length=255)
    disclaimer = serializers.CharField(max_length=500, required=False, allow_null=True)
    timeHeader = serializers.CharField(max_length=100)
    descriptionHeader = serializers.CharField(max_length=100)
    createdAt = serializers.DateTimeField(required=False)
    updatedAt = serializers.DateTimeField(required=False)
    publishedAt = serializers.DateTimeField(required=False)
    documentId = serializers.CharField(max_length=255, required=False)
    locale = serializers.CharField(max_length=10, required=False, allow_null=True)
    timelineEntries = TimelineEntrySerializer(many=True)


class WebcastSerializer(serializers.Serializer):
    """Serializer for webcast data"""
    id = serializers.IntegerField()
    videoId = serializers.CharField(max_length=255)
    streamingVideoType = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=255, required=False, allow_null=True)
    date = serializers.DateField(required=False, allow_null=True)
    isFeatured = serializers.BooleanField(required=False, allow_null=True)
    imageDesktop = ImageSerializer(required=False, allow_null=True)
    imageMobile = ImageSerializer(required=False, allow_null=True)


class ParagraphSerializer(serializers.Serializer):
    """Serializer for paragraph content"""
    id = serializers.IntegerField()
    content = serializers.CharField()


class AstronautSerializer(serializers.Serializer):
    """Serializer for astronaut data"""
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    bioLink = serializers.URLField(required=False, allow_null=True)
    description = serializers.CharField(max_length=255, required=False, allow_null=True)
    portrait = ImageSerializer(required=False, allow_null=True)


class CarouselItemSerializer(serializers.Serializer):
    """Serializer for carousel item data"""
    id = serializers.IntegerField()
    caption = serializers.CharField(max_length=500, required=False, allow_null=True)
    imageDesktop = ImageSerializer(required=False, allow_null=True)
    imageMobile = ImageSerializer(required=False, allow_null=True)
    videoDesktop = serializers.JSONField(required=False, allow_null=True)
    videoMobile = serializers.JSONField(required=False, allow_null=True)


class CarouselSerializer(serializers.Serializer):
    """Serializer for carousel data"""
    id = serializers.IntegerField()
    carouselItems = CarouselItemSerializer(many=True, required=False)


class LaunchDetailSerializer(serializers.Serializer):
    """Serializer for detailed launch information"""
    id = serializers.IntegerField()
    documentId = serializers.CharField(max_length=255)
    correlationId = serializers.CharField(max_length=255, required=False, allow_null=True)
    missionId = serializers.CharField(max_length=255, required=False, allow_null=True)
    title = serializers.CharField(max_length=255)
    subtitle = serializers.CharField(max_length=255, required=False, allow_null=True)
    callToAction = serializers.CharField(max_length=50)
    quickDetail = serializers.CharField(max_length=500, required=False, allow_null=True)
    endDate = serializers.DateField(required=False, allow_null=True)
    youtubeVideoId = serializers.CharField(max_length=255, required=False, allow_null=True)
    streamingVideoType = serializers.CharField(max_length=100, required=False, allow_null=True)
    missionStatus = serializers.CharField(max_length=50)
    followDragonEnabled = serializers.BooleanField()
    returnFromIssEnabled = serializers.BooleanField()
    toTheIssEnabled = serializers.BooleanField()
    toTheIssTense = serializers.CharField(max_length=50, required=False, allow_null=True)
    imageDesktop = ImageSerializer(required=False, allow_null=True)
    imageMobile = ImageSerializer(required=False, allow_null=True)
    videoDesktop = serializers.JSONField(required=False, allow_null=True)
    videoMobile = serializers.JSONField(required=False, allow_null=True)
    infographicDesktop = ImageSerializer(required=False, allow_null=True)
    infographicMobile = ImageSerializer(required=False, allow_null=True)
    preLaunchTimeline = TimelineSerializer(required=False, allow_null=True)
    postLaunchTimeline = TimelineSerializer(required=False, allow_null=True)
    astronauts = AstronautSerializer(many=True, required=False)
    webcasts = WebcastSerializer(many=True, required=False)
    paragraphs = ParagraphSerializer(many=True, required=False)
    carousel = CarouselSerializer(required=False, allow_null=True)
