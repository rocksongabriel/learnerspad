from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Note(models.Model):
    """
    Model for notes
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=300, null=False, blank=False)
    body = models.TextField(blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]

