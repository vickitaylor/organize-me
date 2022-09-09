from unittest.util import _MAX_LENGTH
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=60)
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="room_user")
    picture = models.ImageField(upload_to='room_images', height_field=None, width_field=None, max_length=None, null=True)
    private = models.BooleanField(default=False)
