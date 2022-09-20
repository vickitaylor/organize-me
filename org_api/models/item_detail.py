from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class ItemDetail(models.Model):
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="detail_item")
    room = models.ForeignKey(
        "Room", on_delete=models.CASCADE, related_name="room")
    quantity = models.PositiveIntegerField(default=1, null=True, blank=True)
    receipt_pic = models.ImageField(upload_to='receipt_images', height_field=None, width_field=None, max_length=None,
                                    null=True, blank=True, default="receipt_images/None--f8422ba8-06dd-4ad1-abea-f3f340ec3262.png")
    purchased_from = models.CharField(max_length=55, null=True, blank=True)
    price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(7500.00)], default=0)
    status = models.ForeignKey(
        "Status", on_delete=models.CASCADE, related_name="status", null=True, blank=True)
    serial_num = models.CharField(max_length=55, null=True, blank=True)
    purchase_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)
    expiration_date = models.DateField(
        auto_now=False, auto_now_add=False, null=True, blank=True)

    @property
    def exp_date(self):
        return self.expiration_date.strftime("%m/%d/%Y")

    @property
    def purchased_date(self):
        return self.purchase_date.strftime("%m/%d/%Y")
