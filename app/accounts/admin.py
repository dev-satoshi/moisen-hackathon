from django.contrib import admin

from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "is_staff", "is_active", "date_joined")


admin.site.register(CustomUser, CustomUserAdmin)
