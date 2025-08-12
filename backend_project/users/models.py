from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserMFA(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mfa')
    totp_secret = models.CharField(max_length=64, blank=True, null=True)
    mfa_enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"MFA - {self.user.username}"