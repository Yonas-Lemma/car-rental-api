# cars_api/serializers.py

from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    features = serializers.ReadOnlyField()
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Car
        fields = ['id', 'name', 'make', 'model', 'description', 'price', 'image', 'status', 'features']
    
    def get_image(self, obj):
        """Get the full URL for the image"""
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None