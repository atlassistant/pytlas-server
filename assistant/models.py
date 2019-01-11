from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  language = models.CharField(max_length=10, default='fr-FR')

def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)