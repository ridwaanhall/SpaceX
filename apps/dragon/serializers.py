from rest_framework import serializers


class DragonRawDataSerializer(serializers.Serializer):
    """
    Serializer for Dragon GPS tracking data that preserves the original field names
    from the SpaceX API response.
    """
    
    # GPS and mission time with original field names
    glass_dragon_gps_time_f64 = serializers.FloatField(required=False, allow_null=True)
    glass_dragon_mission_time_f64 = serializers.FloatField(required=False, allow_null=True)
    
    # Dragon position and speed with original field names
    glass_dgn_alt_geod_f64 = serializers.FloatField(required=False, allow_null=True)
    glass_dgn_speed_f64 = serializers.FloatField(required=False, allow_null=True)
    
    # ISS prediction coordinates with original field names
    glass_predict_iss_r_lla_v3 = serializers.ListField(
        child=serializers.FloatField(),
        required=False,
        allow_empty=True,
        allow_null=True
    )
    glass_predict_iss_r_ecef_v3 = serializers.ListField(
        child=serializers.FloatField(),
        required=False,
        allow_empty=True,
        allow_null=True
    )
    
    # Dragon prediction coordinates with original field names
    glass_predict_dgn_r_lla_v3 = serializers.ListField(
        child=serializers.FloatField(),
        required=False,
        allow_empty=True,
        allow_null=True
    )
    glass_predict_dgn_r_ecef_v3 = serializers.ListField(
        child=serializers.FloatField(),
        required=False,
        allow_empty=True,
        allow_null=True
    )
    
    # ISS propagation data (array of coordinate arrays) with original field name
    glass_prop_iss_r_ecef_v3 = serializers.ListField(
        child=serializers.ListField(child=serializers.IntegerField()),
        required=False,
        allow_empty=True,
        allow_null=True
    )
    
    # Dragon propagation data (array of coordinate arrays) with original field name
    glass_prop_dgn_r_ecef_v3 = serializers.ListField(
        child=serializers.ListField(child=serializers.IntegerField()),
        required=False,
        allow_empty=True,
        allow_null=True
    )

    def to_internal_value(self, data):
        """
        Convert the dotted field names from the API to underscored field names for serialization
        """
        converted_data = {}
        field_mapping = {
            'glass.dragon.gps_time_f64': 'glass_dragon_gps_time_f64',
            'glass.dragon.mission_time_f64': 'glass_dragon_mission_time_f64',
            'glass.dgn_alt_geod_f64': 'glass_dgn_alt_geod_f64',
            'glass.dgn_speed_f64': 'glass_dgn_speed_f64',
            'glass.predict_iss_r_lla_v3': 'glass_predict_iss_r_lla_v3',
            'glass.predict_iss_r_ecef_v3': 'glass_predict_iss_r_ecef_v3',
            'glass.predict_dgn_r_lla_v3': 'glass_predict_dgn_r_lla_v3',
            'glass.predict_dgn_r_ecef_v3': 'glass_predict_dgn_r_ecef_v3',
            'glass.prop_iss_r_ecef_v3': 'glass_prop_iss_r_ecef_v3',
            'glass.prop_dgn_r_ecef_v3': 'glass_prop_dgn_r_ecef_v3'
        }
        
        for api_field, serializer_field in field_mapping.items():
            if api_field in data:
                converted_data[serializer_field] = data[api_field]
        
        return super().to_internal_value(converted_data)

    def to_representation(self, instance):
        """
        Convert the data back to the original field names with dots
        """
        data = super().to_representation(instance)
        
        # Convert field names back to the original format with dots
        original_format = {}
        field_mapping = {
            'glass_dragon_gps_time_f64': 'glass.dragon.gps_time_f64',
            'glass_dragon_mission_time_f64': 'glass.dragon.mission_time_f64',
            'glass_dgn_alt_geod_f64': 'glass.dgn_alt_geod_f64',
            'glass_dgn_speed_f64': 'glass.dgn_speed_f64',
            'glass_predict_iss_r_lla_v3': 'glass.predict_iss_r_lla_v3',
            'glass_predict_iss_r_ecef_v3': 'glass.predict_iss_r_ecef_v3',
            'glass_predict_dgn_r_lla_v3': 'glass.predict_dgn_r_lla_v3',
            'glass_predict_dgn_r_ecef_v3': 'glass.predict_dgn_r_ecef_v3',
            'glass_prop_iss_r_ecef_v3': 'glass.prop_iss_r_ecef_v3',
            'glass_prop_dgn_r_ecef_v3': 'glass.prop_dgn_r_ecef_v3'
        }
        
        for serializer_field, original_field in field_mapping.items():
            if serializer_field in data and data[serializer_field] is not None:
                original_format[original_field] = data[serializer_field]
        
        return original_format


class DragonTrackingSerializer(serializers.Serializer):
    """Serializer for Dragon GPS tracking data with readable field names"""
    
    # GPS and mission time
    gps_time = serializers.FloatField(source='glass.dragon.gps_time_f64')
    mission_time = serializers.FloatField(source='glass.dragon.mission_time_f64')
    
    # Dragon position and speed
    altitude_geodetic = serializers.FloatField(source='glass.dgn_alt_geod_f64')
    speed = serializers.FloatField(source='glass.dgn_speed_f64')
    
    # ISS prediction coordinates
    predict_iss_lla = serializers.ListField(
        child=serializers.FloatField(),
        source='glass.predict_iss_r_lla_v3'
    )
    predict_iss_ecef = serializers.ListField(
        child=serializers.FloatField(),
        source='glass.predict_iss_r_ecef_v3'
    )
    
    # Dragon prediction coordinates
    predict_dragon_lla = serializers.ListField(
        child=serializers.FloatField(),
        source='glass.predict_dgn_r_lla_v3'
    )
    predict_dragon_ecef = serializers.ListField(
        child=serializers.FloatField(),
        source='glass.predict_dgn_r_ecef_v3'
    )
    
    # ISS propagation data (array of coordinate arrays)
    propagation_iss_ecef = serializers.ListField(
        child=serializers.ListField(child=serializers.IntegerField()),
        source='glass.prop_iss_r_ecef_v3'
    )
    
    # Dragon propagation data (array of coordinate arrays)
    propagation_dragon_ecef = serializers.ListField(
        child=serializers.ListField(child=serializers.IntegerField()),
        source='glass.prop_dgn_r_ecef_v3'
    )
    
    def to_representation(self, instance):
        """Custom representation to add computed fields and better formatting"""
        data = super().to_representation(instance)
        
        # Add human-readable fields
        data['mission_time_formatted'] = self._format_mission_time(data.get('mission_time'))
        data['altitude_km'] = round(data.get('altitude_geodetic', 0) / 1000, 2) if data.get('altitude_geodetic') else None
        data['speed_ms'] = round(data.get('speed', 0), 2) if data.get('speed') else None
        data['speed_kmh'] = round(data.get('speed', 0) * 3.6, 2) if data.get('speed') else None
        
        # Add coordinate summary
        if data.get('predict_iss_lla') and len(data['predict_iss_lla']) >= 3:
            data['iss_coordinates'] = {
                'latitude': round(data['predict_iss_lla'][0], 6),
                'longitude': round(data['predict_iss_lla'][1], 6),
                'altitude_m': round(data['predict_iss_lla'][2], 2)
            }
        
        if data.get('predict_dragon_lla') and len(data['predict_dragon_lla']) >= 3:
            data['dragon_coordinates'] = {
                'latitude': round(data['predict_dragon_lla'][0], 6),
                'longitude': round(data['predict_dragon_lla'][1], 6),
                'altitude_m': round(data['predict_dragon_lla'][2], 2)
            }
        
        # Add data counts
        data['iss_propagation_points'] = len(data.get('propagation_iss_ecef', []))
        data['dragon_propagation_points'] = len(data.get('propagation_dragon_ecef', []))
        
        return data
    
    def _format_mission_time(self, mission_time_seconds):
        """Convert mission time seconds to human readable format"""
        if not mission_time_seconds:
            return None
            
        hours = int(mission_time_seconds // 3600)
        minutes = int((mission_time_seconds % 3600) // 60)
        seconds = int(mission_time_seconds % 60)
        
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


class DragonSummarySerializer(serializers.Serializer):
    """Simplified serializer for Dragon tracking summary"""
    
    mission_time_formatted = serializers.CharField()
    altitude_km = serializers.FloatField()
    speed_kmh = serializers.FloatField()
    iss_coordinates = serializers.DictField()
    dragon_coordinates = serializers.DictField()
    iss_propagation_points = serializers.IntegerField()
    dragon_propagation_points = serializers.IntegerField()
    last_update = serializers.DateTimeField()
