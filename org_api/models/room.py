from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=60)
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="room_user")
    picture = models.CharField(max_length=500)
    private = models.BooleanField(default=False)
