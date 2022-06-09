from django.contrib import admin

from .models import Brand, Car

admin.site.register(Brand)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_filter = ['brand']