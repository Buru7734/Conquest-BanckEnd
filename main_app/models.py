from django.db import models
from datetime import date
from django.contrib.auth.models import User

CHARACTERS = (
    ('A', 'Holy Paladin'),
    ('B', 'Primal Barbarian'),
    ('C', 'Dragon Knight'),
    ('D', 'Shadow Assassin'),
    ('E', 'Demon Hunter'),
    ('F', 'Chackie Jan'),
    ('G', 'Hasidic Warrior'),
    ('H', 'Mexican Vaquero'),
    ('I', 'Death Knight'),
    ('J', 'Every Italian Ever')

)
SHIELDS = (
    ('S1', 'Oceans Defender'),
    ('S2', 'Skyward Kite'),
    ('S3', 'Earthguard Tower'),
    ('S4', 'Aether Guard Shield'),
    ('S5', 'Correded Heater'),
    ('S6', 'Ironbound Wooden Shield'),
    ('S7', 'Leostrong Bastion'),
    ('S8', 'Mechanum Defender'),
    ('S9', 'Nightfeather Bulwark'),
    ('S10', 'Plainsteel Buckler'),
    ('S11', 'Serpentbloom Aegis'),
    ('S12', 'Bloodborn Edgeguard')

)
WEAPONS = (
    ('W1', 'Natures Chopper'),
    ('W2', 'Fireborn Spear'),
    ('W3', 'Frostblade Claymore'),
    ('W4', 'Battleworn Hatchet'),
    ('W5', 'Common Broadsword'),
    ('W6', 'Forgebreak Polearm'),
    ('W7', 'Ironclad Shortblade'),
    ('W8', 'Nightslayers Scimitar'),
    ('W9', 'Plaugeringers Scythe'),
    ('W10', 'Shadowborn Blade'),
    ('W11', 'Shadowfeather Dagger'),
    ('W12', 'Solaris Glaive')
)

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    weapon = models.CharField(
        max_length=3,
        choices=WEAPONS,
        default=WEAPONS[0][0]
    )
    strength = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    cost = models.IntegerField()
    def __str__(self):
        return self.name

class Shield(models.Model):
    name = models.CharField(max_length=50)
    shield = models.CharField(
        max_length=3,
        choices=SHIELDS,
        default=SHIELDS[0][0]
    )
    strength = models.IntegerField()
    defense = models.IntegerField()
    speed = models.IntegerField()
    cost = models.IntegerField()
    
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
    amount = models.IntegerField(default=10)
    
    def __str__(self):
        return self.amount

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username