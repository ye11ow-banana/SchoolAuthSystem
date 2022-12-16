from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Worker, TeacherType


@receiver([pre_save, post_save], sender=Worker)
def change_state(sender, instance, **kwargs):
    print('Change state method!')
