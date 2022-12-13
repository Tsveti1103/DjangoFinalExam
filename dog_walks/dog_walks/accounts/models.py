from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User, PermissionsMixin
from django.core import validators
from django.db import models
from dog_walks.accounts.managers import AppUserManager
from dog_walks.core.validators import only_cyrillic_letters_validator


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    is_staff = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    objects = AppUserManager()

    USERNAME_FIELD = 'email'


class Profile(models.Model):
    DOG_NAME_MAX_LENGTH = 30
    RESIDENCE_MAX_LENGTH = 50
    USERNAME_MAX_LENGTH = 30
    USERNAME_MIN_LENGTH = 3

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        verbose_name='Потеребителско име:',
        validators=[validators.MinLengthValidator(USERNAME_MIN_LENGTH,
                                                  message='Потеребителското име трябва да съдържа поне 3 символа'),
                    ],
    )
    profile_image = models.ImageField(
        upload_to='users-pic',
        null=True,
        blank=True,
    )
    dog_name = models.CharField(
        max_length=DOG_NAME_MAX_LENGTH,
    )
    residence = models.CharField(
        max_length=RESIDENCE_MAX_LENGTH,
        validators=[only_cyrillic_letters_validator]
    )
    user = models.OneToOneField(
        AppUser,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    have_permission_to_comment = models.BooleanField(
        default=True
    )
