from django.contrib.auth import get_user_model
from django.db.models import signals
from django.dispatch import receiver
from dog_walks.accounts.models import Profile


UserModel = get_user_model()


@receiver(signals.post_save, sender=UserModel)
def create_profile_signal(instance, created, **kwargs):
    if not created:
        return
    Profile.objects.create(user_id=instance.pk)


@receiver(signals.post_save, sender=UserModel)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
