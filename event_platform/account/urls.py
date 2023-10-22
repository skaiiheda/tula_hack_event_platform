from django.urls import path, include
from .views import LogoutView

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('register/participant', views.participant_register, name='participant_register'),
    path('register/organizer', views.organizer_register, name='organizer_register'),
    path('edit/participant', views.edit_participant, name='participant_edit'),
    path('edit/organizer', views.edit_organizer, name='organizer_edit'),
    path("logout/", LogoutView.as_view(), name="logout"),
path('', include('django.contrib.auth.urls')),
]
