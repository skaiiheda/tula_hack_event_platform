from django.db import models
from django.conf import settings


class ParticipantProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    categories = models.ManyToManyField(to="recommendations.Category", null=True, blank=True,
                                        through='recommendations.UserPreferences')
    events = models.ManyToManyField(to="recommendations.Events", through='recommendations.EventRegister')
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)


class OrganizerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    organization = models.CharField(max_length=100, null=True, blank=True, unique=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
