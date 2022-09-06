from django.db import models

class ShoppingItem(models.Model):
    shopping_list = models.ForeignKey(
        "ShoppingList", on_delete=models.CASCADE, related_name="shop_list")
    item = models.ForeignKey(
        "Item", on_delete=models.CASCADE, related_name="shop_list_item")
