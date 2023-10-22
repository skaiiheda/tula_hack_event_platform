from . import views
from django.urls import path

urlpatterns = [
    path('', views.UnloggedEventsListView.as_view(), name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='details'),
    path('event/register/<int:pk>', views.register_to_event, name='reg'),
    path('event/create/', views.EventCreateView.as_view(), name='event_create'),
    path('event/<int:pk>/delete', views.EventDeleteView.as_view(), name='delete'),
]
