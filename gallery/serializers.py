from rest_framework import serializers
from .models import User, Artist, Artwork, Cart, Order

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'user_type']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'bio', 'user']

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ['id', 'title', 'description', 'price', 'artist', 'created_at']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'user', 'artwork', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'cart', 'ordered_at', 'status']
