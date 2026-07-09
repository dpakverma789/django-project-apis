from django.contrib import admin
from .models import *

# admin.site.register(models.BookingDetails)
# admin.site.register(models.TheaterDetails)
# admin.site.register(models.ShowDetails)

admin.site.register((BookingDetails,TheaterDetails,ShowDetails))