from django.urls import path
from .views import Home, HeroList, HeroDetails, CreateUserView, LoginView, VerifyUserView


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('users/register/', CreateUserView.as_view(), name='register'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/token/refresh/', VerifyUserView.as_view(), name='token_refresh'),
    path('heroes/', HeroList.as_view(), name='hero-list'),
    path('heroes/<int:id>/', HeroDetails.as_view(), name='hero-details')
]