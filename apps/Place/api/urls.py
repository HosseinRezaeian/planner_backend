

from django.urls import path,include

from apps.Place.api.views import PlaceCreateAPIView

urlpatterns = [
    path('places/create-place/', PlaceCreateAPIView.as_view(), name='create-place'),
]