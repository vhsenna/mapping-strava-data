from django.urls import include, path
from .views import *

urlpatterns = [
    path('', base_map, name='Base Map View'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
