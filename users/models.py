from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    enrolled_courses = models.ManyToManyField(Course, related_name='profiles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path) # Open image
        
        # resize image
        if img.height > 32 or img.width > 32:
            output_size = (32, 32)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image