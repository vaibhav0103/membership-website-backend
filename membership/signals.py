from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Membership, Pricing


@receiver(post_save, sender=User) 
def create_membership(sender, instance, created, **kwargs):
    if created:
        user_membership = Membership.objects.create(user=instance)
        print("1st",user_membership)
        # if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
            # new_customer_id = stripe.Customer.create(email=instance.email)
        free_membership = Pricing.objects.get(name='Free')
        print("2nd",free_membership)
            # user_membership.stripe_customer_id = new_customer_id['id']
        user_membership.status = 'active'
        user_membership.pricing = free_membership
        user_membership.save()
