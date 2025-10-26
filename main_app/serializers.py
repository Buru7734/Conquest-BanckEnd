from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Hero, Shield, Weapon, Gold, Profile, BattleLog
from django.contrib.auth.models import User
from django.db.models import Q


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['profile_picture']

class UserSerializer(serializers.ModelSerializer):
    profile_picture = serializers.ImageField(source='profile.profile_picture', required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'profile_picture')
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', {})
        picture = profile_data.get('profile_picture')

        # Ensure profile exists
        profile = getattr(instance, 'profile', None)
        if not profile:
            from .models import Profile
            profile = Profile.objects.create(user=instance)

        if picture:
            profile.profile_picture = picture
            profile.save()

        # Handle password
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

        
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

class BattleLogSerializer(serializers.ModelSerializer):
    winner_name = serializers.CharField(source="winner.username", read_only=True)
    loser_name = serializers.CharField(source="loser.username", read_only=True)
    attacker_name = serializers.CharField(source="attacker.username", read_only=True)
    
    class Meta:
        model = BattleLog
        fields = "__all__"