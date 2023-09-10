from django.contrib import admin
from . import models


@admin.register(models.MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')
