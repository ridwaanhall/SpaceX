from rest_framework import serializers


class SpaceXStatsSerializer(serializers.Serializer):
    """Serializer for SpaceX statistics data"""
    id = serializers.IntegerField()
    documentId = serializers.CharField(max_length=255)
    totalLaunches = serializers.IntegerField()
    totalLandings = serializers.IntegerField()
    totalReflights = serializers.IntegerField()
    
    class Meta:
        fields = ['id', 'documentId', 'totalLaunches', 'totalLandings', 'totalReflights']
