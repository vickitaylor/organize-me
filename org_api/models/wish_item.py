from django.db import models

class WishItem(models.Model):
    wish_list = models.ForeignKey(
        "WishList", on_delete=models.CASCADE, related_name="wish_list")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="wishlist_item")
