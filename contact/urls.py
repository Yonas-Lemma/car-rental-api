from django.urls import path
from .views import ContactView

urlpatterns = [
    path('test/', ContactView.as_view(), name='contact'),
]
