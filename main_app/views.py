from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializers import UserSerializer, HeroSerializer, ShieldSerializer
from .models import Hero, Shield


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
    queryset = Hero.objects.all()
    serializer_class = ShieldSerializer
    
class ShieldDetails(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = ShieldSerializer
    lookup_field = 'id'
    
class addShieldToHero(APIView):
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