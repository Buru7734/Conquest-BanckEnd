from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, HeroSerializer, ShieldSerializer, WeaponSerializer, GoldSerializer
from .models import Hero, Shield, Weapon, Gold


class Home(APIView):
    def get(self, request):
        content = {'message': 'Welcome to Conquest'}
        return Response(content)

    

    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = User.objects.get(username=response.data['username'])
        
        # ✅ Create a corresponding Gold record for the new user
        Gold.objects.get_or_create(user=user, defaults={"amount": 10})
        
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user': response.data
        })             
        
# Create your views here.
class LoginView(APIView):
  permission_classes = [permissions.AllowAny]
  
  def post(self, request):
      username = request.data.get('username')
      password = request.data.get('password')
      user = authenticate(username=username, password=password)
      if user:
          refresh = RefreshToken.for_user(user)
          return Response({
              'refresh': str(refresh),
              'access': str(refresh.access_token),
              'user': UserSerializer(user).data
          })
      return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
  
class VerifyUserView(APIView):
  permission_classes = [permissions.IsAuthenticated] 
  
  def get(self, request):
      user = User.objects.get(username=request.user)
      refresh = RefreshToken.for_user(request.user)
      return Response({
          'refresh': str(refresh),
          'access': str(refresh.access_token),
          'user': UserSerializer(user).data
      })

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'    

class PublicHeroList(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = [permissions.AllowAny]
      
class HeroList(generics.ListCreateAPIView):
    
    serializer_class = HeroSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Hero.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class HeroDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    lookup_field = 'id'
    
class ShieldList(generics.ListCreateAPIView):
    queryset = Shield.objects.all()
    serializer_class = ShieldSerializer
    
class ShieldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shield.objects.all()
    serializer_class = ShieldSerializer
    lookup_field = 'id'
    
class WeaponList(generics.ListCreateAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    
class WeaponDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer
    lookup_field = 'id'
    
class GoldList(generics.ListCreateAPIView):
    serializer_class = GoldSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Ensure only the logged-in user's gold is returned
        return Gold.objects.filter(user=self.request.user)

    def list(self, request, *args, **kwargs):
        # Return a single object instead of a list
        gold = self.get_queryset().first()
        if gold:
            serializer = self.get_serializer(gold)
            return Response(serializer.data)
        return Response({"detail": "No gold record found."}, status=404)


class UserGoldDetails(generics.RetrieveAPIView):
    serializer_class = GoldSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'user_id'
    
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Gold.objects.filter(user=user_id)
    
class GoldDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gold.objects.all()
    serializer_class = GoldSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    
    def perform_create(self, serializer):
        # Only set user on creation
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        # Don’t overwrite user during update
        serializer.save()
    
    # def perform_update(self, serializer):
    #     # Automatically attach the authenticated user
    #     serializer.save(user=self.request.user)

class AddWeaponToHero(APIView):
    def post(self, request, hero_id, weapon_id):
        hero = Hero.objects.get(id=hero_id)
        weapon = Weapon.objects.get(id=weapon_id)
        hero.weapons.add(weapon)
        return Response({'message': f'Weapon {weapon.weapon} added to Hero {hero.name}'})
    
class RemoveWeaponFromHero(APIView):
    def post(self, request, hero_id, weapon_id):
        hero = Hero.objects.get(id=hero_id)
        weapon = Weapon.objects.get(id=weapon_id)
        hero.weapons.remove(weapon)
        return Response({'message': f'Weapon {weapon.weapon} removed from Hero {hero.name}'})  
    
class AddShieldToHero(APIView):
    def post(self, request, hero_id, shield_id):
        hero = Hero.objects.get(id=hero_id)
        shield = Shield.objects.get(id=shield_id)
        hero.shields.add(shield)
        return Response({'message': f'Shield {shield.shield} added to Hero {hero.name}'})
    
class RemoveShieldFromHero(APIView):
    def post(self, request, hero_id, shield_id):
        hero = Hero.objects.get(id=hero_id)
        shield = Shield.objects.get(id=shield_id)
        hero.shields.remove(shield)
        return Response({'message': f'Shield {shield.shield} removed from Hero {hero.name}'})    
    
    