from django.db import models

class Family(models.Model):
    owner = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="owner")
    family_user = models.ForeignKey("Organizer", on_delete=models.CASCADE, related_name="fam_user")
    approved = models.BooleanField(default=False)
