from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


from dog_walks.core.validators import only_cyrillic_letters_validator, OptionalSchemeURLValidator
from dog_walks.places.choices import NightsType, FoodPlacesType, PriceRange, \
    WalkType, WelcomeDog, Difficulty, District

UserModel = get_user_model()


class BasePlaceModel(models.Model):
    NAME_MAX_LENGTH = 100
    CITY_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )
    district = models.CharField(
        choices=District.choices(),
        max_length=District.max_len(),
    )
    city = models.CharField(
        max_length=CITY_MAX_LENGTH,
        validators=[only_cyrillic_letters_validator]
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField()
    website = models.URLField(
        null=True,
        blank=True,
        validators=[OptionalSchemeURLValidator]
    )
    modified_date = models.DateField(
        auto_now=True,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.SET('Несъществуващ'),
    )
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ['longitude', 'latitude']
        abstract = True

    def unique_error_message(self, model_class, unique_check):
        if model_class == type(self) and unique_check == ('longitude', 'latitude'):
            return 'Вече има място на тези координати'
        else:
            return super(BasePlaceModel, self).unique_error_message(model_class, unique_check)


class Night(BasePlaceModel):
    PLACE_TYPE = 'night'
    type = models.CharField(
        choices=NightsType.choices(),
        max_length=NightsType.max_len(),
    )
    price = models.CharField(
        choices=PriceRange.choices(),
        max_length=PriceRange.max_len(),
    )

    beds_count = models.PositiveIntegerField()

    image = models.ImageField(
        upload_to='nights-places'
    )
    phone = PhoneNumberField()
    dog_fee = models.BooleanField(
        default=False,
    )


class Eat(BasePlaceModel):
    PLACE_TYPE = 'eat'

    type = models.CharField(
        choices=FoodPlacesType.choices(),
        max_length=FoodPlacesType.max_len(),
    )
    price = models.CharField(
        choices=PriceRange.choices(),
        max_length=PriceRange.max_len(),
    )
    image = models.ImageField(
        upload_to='eat-places'
    )
    phone = PhoneNumberField(
        null=True,
        blank=True,
    )


class Walk(BasePlaceModel):
    HOLIDAYS_MAX_LENGTH = 50
    PLACE_TYPE = 'walk'

    type = models.CharField(
        choices=WalkType.choices(),
        max_length=WalkType.max_len(),
    )

    dogs_are_welcome = models.CharField(
        choices=WelcomeDog.choices(),
        max_length=WelcomeDog.max_len(),
    )

    entrance_fee = models.BooleanField(
        default=False,
    )
    holidays = models.CharField(
        null=True,
        blank=True,
        max_length=HOLIDAYS_MAX_LENGTH,
    )
    duration = models.TimeField(
        null=True,
        blank=True,
        auto_now=False,
        auto_now_add=False,
    )
    distance = models.FloatField(
        null=True,
        blank=True,
    )
    displacement = models.FloatField(
        null=True,
        blank=True,
    )
    difficulty = models.CharField(
        choices=Difficulty.choices(),
        max_length=Difficulty.max_len(),
    )
    image = models.ImageField(
        upload_to='walk-places'
    )
    phone = PhoneNumberField(
        null=True,
        blank=True,
    )
