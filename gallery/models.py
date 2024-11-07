from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    USER_TYPES = (
        ('Buyer', 'Buyer'),
        ('Seller', 'Seller'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

    def __str__(self):
        return self.username

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='artist_profile')

    def __str__(self):
        return self.name

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='in_carts')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"Cart of {self.user.username} - {self.artwork.title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='orders')
    ordered_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


# Create your models here.
