from django.db import models

# Create your models here.

class Event(models.Model):
    EventName = models.CharField(max_length=45)
    EventVenue = models.CharField(max_length=100)
    EventDescription = models.CharField(max_length=500)
    EventDate = models.DateField()
    EventTime = models.TimeField( auto_now=False, auto_now_add=False)
    EventAvailableTickets = models.IntegerField()
