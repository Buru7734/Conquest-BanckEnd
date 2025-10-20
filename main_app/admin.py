from django.contrib import admin
from .models import Weapon, Shield, Hero

# Register your models here.
admin.site.register(Hero)
admin.site.register(Weapon)
admin.site.register(Shield)
