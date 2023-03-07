from django.contrib import admin
from employees.models import Bookings, Test, Favorite_places
# Register your models here.
admin.site.register(Bookings)
admin.site.register(Test)
admin.site.register(Favorite_places)
