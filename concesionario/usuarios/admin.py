from django.contrib import admin

from usuarios.models import (
    Province,
    Location,
    StandardUser,
)


@admin.register(Location)
class LocalidadAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(Province)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )

@admin.register(StandardUser)
class StandardUserAdmin(admin.ModelAdmin):
    list_display = (
        'user',
    )
