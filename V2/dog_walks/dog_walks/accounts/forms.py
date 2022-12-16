from django import forms
from django.contrib.auth.forms import PasswordChangeForm

from dog_walks.accounts.models import Profile
from django.contrib.auth import forms as auth_forms, get_user_model
from dog_walks.core.utils import field_required_error
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

UserModel = get_user_model()


class AdminRegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label="Парола:",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Повтори паролата:",
        # TODO remove autocomplete after the exam
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    error_messages = {
        'password_mismatch': 'Паролите не съвпадат!',
    }
    email = forms.EmailField(
        label='Имейл',
    )

    def __init__(self, *args, **kwargs):
        super(AdminRegisterUserForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())

    def clean_email(self):
        email = self.cleaned_data['email']
        users = UserModel.objects.filter(email__iexact=email)
        if users:
            raise forms.ValidationError("Вече има регистриран потребител с този имейл")
        return email

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2',)


class RegisterUserForm(auth_forms.UserCreationForm):
    password1 = forms.CharField(
        label="Парола:",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    password2 = forms.CharField(
        label="Повтори паролата:",
        # TODO remove autocomplete after the exam
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    error_messages = {
        'password_mismatch': 'Паролите не съвпадат!',
    }
    email = forms.EmailField(
        label='Имейл',
    )
    agree = forms.BooleanField(label='Съгласен съм с правилата ', required=True,
                               disabled=False,
                               error_messages={'required': 'Моля съгласете се с правилата'})

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())

    def clean_email(self):
        email = self.cleaned_data['email']
        users = UserModel.objects.filter(email__iexact=email)
        if users:
            raise forms.ValidationError("Вече има регистриран потребител с този имейл")
        return email

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'agree',)


class LoginUserForm(auth_forms.AuthenticationForm):
    password = forms.CharField(
        label="Парола:",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )
    username = forms.EmailField(
        label='Имейл',
    )
    error_messages = {
        'invalid_login':
            "Грешни потребителско име или парола"
    }
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())

    def __init__(self, *args, **kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'dog_name', 'profile_image', 'residence']
        error_message = {'required': 'Моля попълнете полето'}
        labels = {
            'username': 'Потребителско име',
            'dog_name': 'Име на кучето',
            'profile_image': 'Профилна снимка',
            'residence': 'Местожителство',
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())


class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Стара парола",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label="Нова парола:",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    new_password2 = forms.CharField(
        label="Повтори паролата:",
        # TODO remove autocomplete after the exam
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    error_messages = {
        'password_mismatch': 'Паролите не съвпадат!',
        'password_incorrect': "Вашата стара парола е грешна. Моля въведете отново.",

    }

    def __init__(self, *args, **kwargs):
        super(MyPasswordChangeForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())
