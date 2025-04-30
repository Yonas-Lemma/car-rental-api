# from django.db import models

# class Car(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name
    



    ####################
    # cars_api/models.py

from django.db import models

class Car(models.Model):
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('maintenance', 'Maintenance'),
    )
    
    name = models.CharField(max_length=100)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', null=True, blank=True)

    def get_image_url(self):
        """Return the full URL for the image"""
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None


    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    
    # Car features
    engine = models.CharField(max_length=50, null=True, blank=True)
    transmission = models.CharField(max_length=50, null=True, blank=True)
    fuel_type = models.CharField(max_length=50, null=True, blank=True)
    mileage = models.IntegerField(null=True, blank=True)
    color = models.CharField(max_length=30, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    
    @property
    def features(self):
        """Return car features as a dictionary for the API"""
        return {
            'year': self.year,
            'engine': self.engine,
            'transmission': self.transmission,
            'fuelType': self.fuel_type
        }