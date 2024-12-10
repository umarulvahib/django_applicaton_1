from django.db.models.signals import post_save
from django.dispatch import receiver

from store.models import Category


@receiver(post_save, sender=Category)
def post_save_create_category_receiver(sender, instance, created, **kwargs):
    print('create project', instance)
