from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    private = models.BooleanField(default=False)
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="event_user")
