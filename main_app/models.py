from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.
from django.contrib.auth.models import User

CHARACTERS = (
    ('A', 'A_one'),
    ('B', 'B_two'),
    ('C', 'C_three'),
    ('D', 'D_four'),
    ('E', 'E_five')
              )

SHIELDS = (
    ('S1', 'Shield1'),
    ('S2', 'Shield2'),
    ('S3', 'Shield3')
)

WEAPONS = (
    ('W1', 'weapon1'),
    ('W2', 'weapon2'),
    ('W3', 'weapon3')
)

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    weapon = models.CharField(
        max_length=2,
        choices=WEAPONS,
        default=WEAPONS[0][0]
    )
    
    def __str__(self):
        return self.name

class Shield(models.Model):
    name = models.CharField(max_length=50)
    shield = models.CharField(
        max_length=2,
        choices=SHIELDS,
        default=SHIELDS[0][0]
    )
    
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
    
