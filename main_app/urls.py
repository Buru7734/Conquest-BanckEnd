from django.urls import path
from .views import Home, HeroList, HeroDetails,ShieldList,AddShieldToHero,RemoveShieldFromHero, ShieldDetails,WeaponList, WeaponDetails, AddWeaponToHero, RemoveWeaponFromHero,GoldDetails,GoldList, CreateUserView, LoginView, VerifyUserView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('heroes/', HeroList.as_view(), name='hero-list'),
    path('heroes/<int:id>/', HeroDetails.as_view(), name='hero-details'),
    path('shields/', ShieldList.as_view(), name='Shield-List'),
    path('shields/<int:id>/', ShieldDetails.as_view(), name='Shield-details'),
    path('heroes/<int:hero_id>/add_shield/<int:shield_id>/', AddShieldToHero.as_view(), name='add-shield-to-hero'),
    path('heroes/<int:hero_id>/remove_shield/<int:shield_id>/', RemoveShieldFromHero.as_view(), name='add-shield-to-hero'),
    path('weapons/', WeaponList.as_view(), name='weapons-List'),
    path('weapons/<int:id>/',WeaponDetails.as_view(), name='weapons-details'),
    path('heroes/<int:hero_id>/add_weapon/<int:weapon_id>/',AddWeaponToHero.as_view(), name='add-weapons'),
    path('heroes/<int:hero_id>/remove_weapon/<int:weapon_id>/',RemoveWeaponFromHero.as_view(), name='remove-weapons'),
    path('gold/',GoldList.as_view(), name='gold-list'),
    path('gold/<int:id>/',GoldDetails.as_view(), name='gold-details')
    
]