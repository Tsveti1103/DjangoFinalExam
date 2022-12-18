from django import forms
from dog_walks.common.models import NightComment, EatComment, WalkComment, NightReport, EatReport, WalkReport, ContactUs


class NightReportForm(forms.ModelForm):
    class Meta:
        model = NightReport
        fields = ('description',)
        labels = {
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 50,
                    'rows': 10,
                    'placeholder': 'Опиши промяната...'
                },
            ),
        }


class EatReportForm(forms.ModelForm):
    class Meta:
        model = EatReport
        fields = ('description',)
        labels = {
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 50,
                    'rows': 10,
                    'placeholder': 'Опиши промяната...'
                },
            ),
        }


class WalkReportForm(forms.ModelForm):
    class Meta:
        model = WalkReport
        fields = ('description',)
        labels = {
            'description': 'Описание',
        }
        widgets = {
            'description': forms.Textarea(
                attrs={
                    'cols': 50,
                    'rows': 10,
                    'placeholder': 'Опиши промяната...'
                },
            ),
        }


class NightsCommentForm(forms.ModelForm):
    class Meta:
        model = NightComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 5,
                    'placeholder': 'Добави коментар...'
                },
            ),
        }


class EatCommentForm(forms.ModelForm):
    class Meta:
        model = EatComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 5,
                    'placeholder': 'Добави коментар...'
                },
            ),
        }


class WalkCommentForm(forms.ModelForm):
    class Meta:
        model = WalkComment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'cols': 40,
                    'rows': 5,
                    'placeholder': 'Добави коментар...'
                },
            ),
        }


class ContactUserForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ('description', 'email')
        labels = {
            'description': 'Текст',
            'email': 'Имейл',
        }

    # TODO remove this and make field i the model blank True if don't find a way to do required False if user
    def __init__(self, *args, **kwargs):
        super(ContactUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
