# cars_api/views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer

class CarViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cars to be viewed or edited.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    
    def list(self, request):
        """
        Override list method to return only available cars by default
        """
        # Get query parameters
        status_filter = request.query_params.get('status', None)
        
        if status_filter:
            queryset = Car.objects.filter(status=status_filter)
        else:
            # By default, return all cars
            queryset = Car.objects.all()
            
        serializer = CarSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)