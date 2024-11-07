from django.contrib import admin
from .models import User, Artist, Artwork, Cart, Order

# Register each model
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Artwork)
admin.site.register(Cart)
admin.site.register(Order)
