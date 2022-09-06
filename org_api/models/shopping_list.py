from django.db import models

class ShoppingList(models.Model):
    org = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="organizer")
    private = models.BooleanField(default=False)
