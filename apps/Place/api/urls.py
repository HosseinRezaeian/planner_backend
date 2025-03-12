

from django.urls import path,include

from apps.Place.api.views import PlaceCreateAPIView, PlaceListAPIView, PlaceUpdate

urlpatterns = [
    path('places/create-place/', PlaceCreateAPIView.as_view(), name='create-place'),
    path('places/list/', PlaceListAPIView.as_view(), name='places-list'),
    path('places/update/<str:place_id>/', PlaceUpdate.as_view(), name='places-update'),
]