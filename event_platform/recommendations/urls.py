from . import views
from django.urls import path

urlpatterns = [
    path('', views.UnloggedEventsListView.as_view(), name='index'),
    path('event/<int:pk>', views.EventDetailView.as_view(), name='details'),
    path('event/register/<int:pk>', views.register_to_event, name='reg')
]
