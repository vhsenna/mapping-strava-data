from django.urls import include, path
from .views import *

urlpatterns = [
    path('', base_map, name='base map view'),
    path('connected/', connected_map, name='connect map view'),
    path('oauth/', include('social_django.urls', namespace='social')),
]
