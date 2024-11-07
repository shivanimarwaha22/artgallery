from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework import viewsets
from .models import User, Artist, Artwork, Cart, Order
from .serializers import UserSerializer, ArtistSerializer, ArtworkSerializer, CartSerializer, OrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can manage users
    throttle_classes = [UserRateThrottle]

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view and manage artists
    throttle_classes = [UserRateThrottle]

class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer
    throttle_classes = [UserRateThrottle, AnonRateThrottle]  # Custom throttle settings if needed

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can manage their cart
    throttle_classes = [UserRateThrottle]

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can view and manage orders
    throttle_classes = [UserRateThrottle]



# Create your views here.
