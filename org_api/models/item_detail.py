from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ItemDetail(models.Model):
    item = models.OneToOneField(
        "Item", on_delete=models.CASCADE, related_name="detail_item")
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="room")
    quantity = models.PositiveIntegerField(default=0, null=True, blank=True)
    receipt_pic = models.CharField(max_length=500, null=True, blank=True)
    purchased_from = models.CharField(max_length=55, null=True, blank=True)
    price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(7500.00)], null=True, blank=True)
    status_id = models.ForeignKey(
        "Status", on_delete=models.CASCADE, related_name="status", null=True, blank=True)
    serial_num = models.CharField(max_length=55)
    purchase_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    expiration_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
