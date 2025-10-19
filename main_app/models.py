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

class Shield(models.Model):
    shield = models.CharField(
        max_length=1,
        choices=CHARACTERS,
        default=CHARACTERS[0][0]
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
    character = models.CharField(
        max_length=1,
        choices=CHARACTERS,
        default=CHARACTERS[0][0]
    )

    
    def __str__(self):
        return self.name
    
