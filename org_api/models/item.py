from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=60)
    org = models.ForeignKey(
        "Organizer", on_delete=models.CASCADE, related_name="item_user")
    picture = models.ImageField(upload_to='item_images', height_field=None, width_field=None, max_length=None, null=True)
    private = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="category")
    likes = models.ManyToManyField(
        "Organizer", through="Like", related_name="like_item")
    wish_items = models.ManyToManyField(
        "WishList", through="WishItem", related_name="wishlist_item")
    shopping_items = models.ManyToManyField(
        "ShoppingList", through="ShoppingItem", related_name="shop_list_item")


    @property 
    def liked(self):
        return self.__liked

    @liked.setter 
    def liked(self, value):
        self.__liked = value
