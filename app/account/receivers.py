import uuid
import re

from django.db.models.signals import pre_save
from django.dispatch import receiver
from account.models import User


@receiver(pre_save, sender=User)
def user_lower_email(instance, *args, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_set_username(instance, *args, **kwargs):
    if not instance.pk and not instance.username:
        instance.username = str(uuid.uuid4())


@receiver(pre_save, sender=User)
def user_phone_number(instance, *args, **kwargs):
    if instance.phone_number:
        instance.phone_number = "".join(re.findall(r'\d+', f"{instance.phone_number}"))
