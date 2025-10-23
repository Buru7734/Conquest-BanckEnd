from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hero, Shield, Weapon, Gold
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model= User
        fields = ('id', 'username', 'email', 'password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user
    
        
class ShieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shield
        fields = '__all__'
        
class GoldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gold
        fields = '__all__'
        read_only_fields = ['user']
        
class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'
            
    

class HeroSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    shields = ShieldSerializer(many=True, read_only=True)  
    weapons = WeaponSerializer(many=True, read_only=True)
    
    class Meta:
        model = Hero
        fields = '__all__'
