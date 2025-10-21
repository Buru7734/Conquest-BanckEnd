from django.db import models
from datetime import date
from django.contrib.auth.models import User

CHARACTERS = (
    ('A', 'Holy Paladin'),
    ('B', 'Primal Barbarian'),
    ('C', 'Dragon Knight'),
)
SHIELDS = (
    ('S1', 'Oceans Defender'),
    ('S2', 'Skyward Kite'),
    ('S3', 'Earthguard Tower')
)
WEAPONS = (
    ('W1', 'Natures Chopper'),
    ('W2', 'Fireborn Spear'),
    ('W3', 'Frostblade Claymore')
)

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    weapon = models.CharField(
        max_length=2,
        choices=WEAPONS,
        default=WEAPONS[0][0]
    )
    strength = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    # cost = models.IntegerField()
    def __str__(self):
        return self.name

class Shield(models.Model):
    name = models.CharField(max_length=50)
    shield = models.CharField(
        max_length=2,
        choices=SHIELDS,
        default=SHIELDS[0][0]
    )
    strength = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    # cost = models.IntegerField()
    
    def __str__(self):
        return self.name

class Hero(models.Model):
    name = models.CharField(max_length=50)
    strength = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shields = models.ManyToManyField(Shield)
    weapons = models.ManyToManyField(Weapon)
    character = models.CharField(
        max_length=1,
        choices=CHARACTERS,
        default=CHARACTERS[0][0]
    )
    
    def __str__(self):
        return self.name
    
class Gold(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    
    def __str__(self):
        return self.amount
