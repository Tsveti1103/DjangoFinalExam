from django.contrib.auth.password_validation import MinimumLengthValidator, \
    CommonPasswordValidator, NumericPasswordValidator
from django.core.exceptions import ValidationError


class MyMinimumLengthValidator(MinimumLengthValidator):

    def validate(self, password, user=None):
        if len(password) < self.min_length:
            raise ValidationError(
                "Паролата е тъврде къса. Тя трябва да съдържа поне 8 знака.",
            )


class MyCommonPasswordValidator(CommonPasswordValidator):
    def validate(self, password, user=None):
        if password.lower().strip() in self.passwords:
            raise ValidationError(
                "Тази парола е твърде често срещана.",
            )


class MyNumericPasswordValidator(NumericPasswordValidator):
    def validate(self, password, user=None):
        if password.isdigit():
            raise ValidationError(
                "Тази парола е изцяло цифрова."
            )
