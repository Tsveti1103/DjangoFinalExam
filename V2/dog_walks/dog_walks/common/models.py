from django.contrib.auth import get_user_model
from django.db import models
from dog_walks.places.models import Night, Eat, Walk

UserModel = get_user_model()


class BaseCommentModel(models.Model):
    MAX_TEXT_LENGTH = 300
    text = models.TextField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    is_checked_by_staff = models.BooleanField(default=False)

    class Meta:
        abstract = True


class BaseReportPlace(models.Model):
    description = models.TextField(
        null=False,
        blank=False,
    )
    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=False,
    )
    is_checked_by_staff = models.BooleanField(default=False)

    class Meta:
        abstract = True


class GetUserModel(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class GetNightPlaceModel(models.Model):
    PLACE_TYPE = 'night'
    place = models.ForeignKey(
        Night,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.place.name


class GetEatPlaceModel(models.Model):
    PLACE_TYPE = 'eat'
    place = models.ForeignKey(
        Eat,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.place.name


class GetWalkPlaceModel(models.Model):
    PLACE_TYPE = 'walk'
    place = models.ForeignKey(
        Walk,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.place.name


class NightComment(BaseCommentModel, GetNightPlaceModel, GetUserModel):
    pass


class EatComment(BaseCommentModel, GetEatPlaceModel, GetUserModel):
    pass


class WalkComment(BaseCommentModel, GetWalkPlaceModel, GetUserModel):
    pass


class NightLike(GetUserModel, GetNightPlaceModel):
    pass


class EatLike(GetUserModel, GetEatPlaceModel):
    pass


class WalkLike(GetUserModel, GetWalkPlaceModel):
    pass


class NightWantToVisit(GetUserModel, GetNightPlaceModel):
    pass


class EatWantToVisit(GetUserModel, GetEatPlaceModel):
    pass


class WalkWantToVisit(GetUserModel, GetWalkPlaceModel):
    pass


class NightReport(BaseReportPlace, GetNightPlaceModel, GetUserModel):
    pass


class EatReport(BaseReportPlace, GetEatPlaceModel, GetUserModel):
    pass


class WalkReport(BaseReportPlace, GetWalkPlaceModel, GetUserModel):
    pass


class ContactUs(BaseReportPlace):
    email = models.EmailField(
    )

    def __str__(self):
        return self.email
