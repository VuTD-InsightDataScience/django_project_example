from django.db.models.signals import post_delete, post_save, pre_delete, pre_save
from django.dispatch import receiver

from example_app.models import Example


@receiver(pre_save, sender=Example)
def handle_pre_save_example(sender, instance, **kwargs):
    """ Handle before saving instance """
    pass






@receiver(post_save, sender=Example)
def handle_post_save_example(sender, instance, created, **kwargs):
    """ Handle when created or updated instance successfully """
    if created:
        print('Created new example')


@receiver(pre_delete, sender=Example)
def handle_pre_delete_example(sender, instance, **kwargs):
    """ Handle before deleted instance """
    if instance.live:
        instance.unpublish(commit=False)


@receiver(post_delete, sender=Example)
def handle_post_delete_example(sender, instance, **kwargs):
    """ Handle when instance is deleted """
    pass
