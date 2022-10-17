from django.db.models.signals import pre_save
from django.dispatch import receiver
from Transfer.models import Client
from django.utils.text import slugify


@receiver(pre_save, sender = Client)  
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.username)
        instance.slug = slug