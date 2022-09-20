from django.db import models


class Receipt(models.Model):
    item_detail = models.ForeignKey(
        "ItemDetail", on_delete=models.CASCADE, related_name="receipt")
    receipt_pic = models.ImageField(
        upload_to='receipt_images', height_field=None, width_field=None, max_length=None, null=True)
