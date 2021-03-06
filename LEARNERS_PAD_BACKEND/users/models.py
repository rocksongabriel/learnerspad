from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractUser
import uuid

class User(AbstractUser):
    """Custom user model"""
    class Types(models.TextChoices):
        DEVELOPER = "DEVELOPER", "Developer"
        STUDENT = "STUDENT", "Student"

    base_type = Types.STUDENT

    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False, null=False, blank=False)
    type = models.CharField(max_length=40, default=Types.STUDENT, choices=Types.choices)
    avatar = models.ImageField(upload_to="profile/avatar/", null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class DeveloperUserManager(BaseUserManager):
    """Custom manager for the developer user types"""

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.DEVELOPER)


class StudentUserManager(BaseUserManager):
    """Custom manager for the student user types"""

    def get_queryset(self, *args, **kwargs):
        return super(*args, **kwargs).get_queryset().filter(type=User.Types.STUDENT)


class DeveloperUserProfile(models.Model):
    """Profile model for the developer user types"""

    user = models.OneToOneField(
        "users.DeveloperUser",
        on_delete=models.CASCADE,
        related_name="developer_profile"
    )
    bio = models.TextField(max_length=180, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"

class StudentUserProfile(models.Model):
    """Profile model for the student user types"""

    user = models.OneToOneField(
        "users.StudentUser",
        on_delete=models.CASCADE,
        related_name="student_profile"
    )
    bio = models.TextField(max_length=180, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} profile"

class DeveloperUser(User):
    """Proxy model for the developer user type"""

    objects = DeveloperUserManager()

    base_type = User.Types.DEVELOPER

    class Meta:
        proxy = True
        verbose_name = "Developer User"
        verbose_name_plural = "Developer Users"

    @property
    def profile(self):
        return self.developer_profile


class StudentUser(User):
    """Proxy model for the student user type"""

    objects = StudentUserManager()

    base_type = User.Types.STUDENT

    class Meta:
        proxy = True
        verbose_name = "Student User"
        verbose_name_plural = "Student Users"

    def profile(self):
        return self.student_profile


"""
TODO

todo - test the added signals
todo - add an avatar field to the User model
todo - find a way to test the image field
"""