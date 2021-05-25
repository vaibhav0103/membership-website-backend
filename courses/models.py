from django.db import models
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from membership.models import Pricing

class Category(models.Model):
    name= models.CharField(max_length=30)
    desc = models.CharField(max_length=150)


class Course(models.Model):
    title= models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    description = models.TextField()
    pricing_tiers = models.ManyToManyField(Pricing, blank=True)
    categories= models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse("courses:course-detail", kwargs={"slug": self.slug})

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lesson')
    title = models.CharField(max_length=150)
    video_url = models.CharField(max_length=120)
    description = models.TextField()
    order = models.IntegerField(default=1)
    document_url = models.CharField(max_length=120)

    def __str__(self):
        return self.title

def pre_save_course(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(pre_save_course, sender=Course)