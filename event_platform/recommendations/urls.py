from . import views
from . import api_views
from django.urls import path

urlpatterns = [
    path('', views.UnloggedEventsListView.as_view(), name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='details'),
    path('event/register/<int:pk>', views.register_to_event, name='reg'),
    path('api/coordinates', api_views.EventCoordinates.as_view(), name='coords'),
    path('api/coordinates/list', api_views.EventCoordinatesList.as_view(), name='coords_list'),
]
