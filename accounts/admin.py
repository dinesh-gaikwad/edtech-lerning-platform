from django.contrib import admin
from .models import UserSession

@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ['user', 'login_time', 'ip_address']
    readonly_fields = ['user', 'login_time', 'ip_address']