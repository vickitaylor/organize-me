from django.db import models

class WishList(models.Model):
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="wish_user")
    private = models.BooleanField(default=False)
