from django.db import models

class Comment(models.Model):
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="comment_item")
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="comment_user")
    comment = models.CharField(max_length=500)
