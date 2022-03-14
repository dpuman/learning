from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Page


@receiver(post_delete, sender=Page)
def delete_related_user(sender, instance, **kwargs):
    instance.user.delete()
