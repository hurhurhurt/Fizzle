from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django import forms
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="Full Name")
    location = models.CharField(max_length=50, default="Location")
    age = models.PositiveSmallIntegerField(default=18)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    bio = models.TextField(max_length=500, default="Max 500 characters.")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Questions(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    q1 = models.BooleanField(help_text="Does pineapple belong on pizza?", default='True')
    q2 = models.BooleanField(help_text="Are hot dogs sandwiches?", default='True')
    q3 = models.BooleanField(help_text="Are you a morning person?", default='True')
    q4 = models.BooleanField(help_text="Is your background picture is a selfie?", default='True')
    q5 = models.BooleanField(help_text="Did you sit in a different seat each day in class?", default='True')
    q6 = models.BooleanField(help_text="Do you eat pizza crust first?", default='True')
    q7 = models.BooleanField(help_text="Do you pour milk in before the cereal?", default='True')
    q8 = models.BooleanField(help_text="Do you put Christmas decorations on right after Halloween?", default='True')
    q9 = models.BooleanField(help_text="Do you drink ice coffee even in freezing weather?", default='True')

    def __str__(self):
        return f'{self.user.username} Questions'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
