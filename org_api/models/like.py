from django.db import models

class Like(models.Model):
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="like_user")
    item = models.ForeignKey("Item", on_delete=models.CASCADE, related_name="like_item")
