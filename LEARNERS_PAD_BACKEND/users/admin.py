from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import DeveloperUser, StudentUser, User

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "type", "last_login"]
    readonly_fields = ["username", "email", "first_name", "last_name", "type", "last_login", "password", "is_staff", "is_superuser"]

@admin.register(User)
class UserAdmin(UserModelAdmin):
    pass


@admin.register(DeveloperUser)
class DeveloperUserAdmin(UserModelAdmin):
    pass


@admin.register(StudentUser)
class StudentUserAdmin(UserModelAdmin):
    pass