from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'artworks', views.ArtworkViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'orders', views.OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
