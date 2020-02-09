from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="Full Name")
    location = models.CharField(max_length=50, default="Location")
    age = models.PositiveSmallIntegerField(default=18)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
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
    q1 = models.BooleanField(default='True')
    q2 = models.BooleanField(default='True')
    q3 = models.BooleanField(default='True')
    q4 = models.BooleanField(default='True')
    q5 = models.BooleanField(default='True')

    def __str__(self):
        return f'{self.user.username} Questions'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
