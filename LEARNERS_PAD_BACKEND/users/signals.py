from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import (DeveloperUser, DeveloperUserProfile, StudentUser,
                          StudentUserProfile)


@receiver(post_save, sender=DeveloperUser)
def create_developer_user_profile(instance, created, sender, **kwargs):
    """a signal that creates a developer user profile when a developer user is created"""
    if created:
        profile = DeveloperUserProfile.objects.create(user=instance)
        profile.save()


@receiver(post_save, sender=StudentUser)
def create_student_user_profile(instance, created, sender, **kwargs):
    """a signal that creates a student user profile when a student user is created"""
    if created:
        profile = StudentUserProfile.objects.create(user=instance)
        profile.save()