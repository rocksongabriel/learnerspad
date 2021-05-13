from enum import unique
from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Types(models.TextChoices):
        DEVELOPER = "DEVELOPER", "Developer"
        STUDENT = "STUDENT", "Student"

    base_type = Types.STUDENT

    type = models.CharField(max_length=40, default=Types.STUDENT, choices=Types.choices)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class DeveloperUserManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DEVELOPER)


class StudentUserManager(BaseUserManager):

    def get_queryset(self, *args, **kwargs):
        return super(*args, **kwargs).get_queryset().filter(type=User.Types.STUDENT)
class DeveloperUser(User):

    objects = DeveloperUserManager()

    base_type = User.Types.DEVELOPER

    class Meta:
        proxy = True


class StudentUser(User):

    objects = StudentUserManager()

    base_type = User.Types.STUDENT

    class Meta:
        proxy = True