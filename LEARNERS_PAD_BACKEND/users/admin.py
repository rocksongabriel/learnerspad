from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import DeveloperUser, StudentUser, User

class UserModelAdmin(BaseUserAdmin):
    list_display = ["uuid", "username", "email", "first_name", "last_name", "type", "last_login"]


@admin.register(User)
class UserAdmin(UserModelAdmin):
    pass


@admin.register(DeveloperUser)
class DeveloperUserAdmin(UserModelAdmin):
    pass


@admin.register(StudentUser)
class StudentUserAdmin(UserModelAdmin):
    pass