from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', include('django.contrib.auth.urls')),
    path('register/participant', views.participant_register, name='participant_register'),
    path('register/organizer', views.organizer_register, name='organizer_register'),
    path('edit/participant', views.edit_participant, name='participant_edit'),
    path('edit/organizer', views.edit_organizer, name='organizer_edit'),
]
