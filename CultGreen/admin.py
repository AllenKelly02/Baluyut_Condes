from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Profile)
admin.site.register(Plant)
admin.site.register(Watering)
admin.site.register(Sunlight)