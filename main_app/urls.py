from django.urls import path
from .views import Home, HeroList, HeroDetails,ShieldList,AddShieldToHero,RemoveShieldFromHero, UserDetails, ShieldDetails,WeaponList, WeaponDetails, AddWeaponToHero, RemoveWeaponFromHero,GoldDetails,GoldList, CreateUserView, LoginView, VerifyUserView, UserListView, PublicHeroList, UserGoldDetails, BattleLogListView, BattleLogCreateView, UnreadBattleLogsView, mark_battles_as_read


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetails.as_view(), name='user-details'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('heroes/', HeroList.as_view(), name='hero-list'),
    path('heroes/public/', PublicHeroList.as_view(), name='public-hero-list'),
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
    path('gold/<int:id>/',GoldDetails.as_view(), name='gold-details'),
    path('gold/users/<int:user_id>/', UserGoldDetails.as_view(), name='user-gold-list'),
    path("battles/", BattleLogListView.as_view(), name="battle-log-list"),
    path("battles/create/", BattleLogCreateView.as_view(), name="battle-log-create"),
    path("battles/unread/", UnreadBattleLogsView.as_view(), name="battle-log-unread"),
    path("battles/mark-read/", mark_battles_as_read, name="battle-log-mark-read"),
    
    
]