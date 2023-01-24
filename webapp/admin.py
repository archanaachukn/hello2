

# Register your models here.
from django.contrib import admin
from . models import place
from . models import name
admin.site.register(place)
admin.site.register(name)