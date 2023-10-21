from django.db import models
from django.conf import settings
from account.models import OrganizerProfile, ParticipantProfile


class UserPreferences(models.Model):
    profile = models.ForeignKey(ParticipantProfile, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    interest_coef = models.FloatField(default=0.5)


class EventRegister(models.Model):
    profile = models.ForeignKey(ParticipantProfile, on_delete=models.CASCADE)
    event = models.ForeignKey('Events', on_delete=models.CASCADE)
    rated = models.BooleanField(default=False)


class Events(models.Model):
    title = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    date = models.DateTimeField()
    end_reg = models.DateTimeField()
    categories = models.ManyToManyField(to='Category')
    description = models.TextField()
    image = models.ImageField(upload_to='events/images')
    organizer = models.ForeignKey(OrganizerProfile, on_delete=models.SET_NULL, to_field='organization', null=True)


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
