from django.db import models
from django.conf import settings


class Pricing(models.Model):
    name = models.CharField(max_length=100)  # Basic / Pro / Premium
    slug = models.SlugField()
    stripe_price_id = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    currency = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Membership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.SET_NULL, null=True, related_name='memberships')
    created = models.DateTimeField(auto_now_add=True)
    stripe_subscription_id = models.CharField(max_length=50)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.user.email