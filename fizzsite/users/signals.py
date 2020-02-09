from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Questions


@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(user=user)
        profile.save()


@receiver(post_save, sender=User)
def save_question(sender, instance, created, **kwargs):
    user = instance
    if created:
        question = Questions.objects.create(user=user)
        question.save()