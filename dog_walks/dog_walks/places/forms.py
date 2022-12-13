from django import forms
from dog_walks.core.utils import field_required_error
from dog_walks.places.models import Night, Eat, Walk

class CreateNightsPlaceForm(forms.ModelForm):
    class Meta:
        model = Night
        exclude = ('approved', 'user')
        labels = {
            'name': 'Име',
            'district': 'Област',
            'city': 'Населено място',
            'latitude': 'Географска ширина',
            'longitude': 'Географска дължина',
            'description': 'Описание',
            'website': 'Уебсайт',
            'type': 'Вид',
            'price': 'Ценови Диапазон',
            'beds_count': 'Брой места за настаняване',
            'phone': 'Телефон за връзка',
            'image': 'Снимка',
            'dog_fee': 'Допълнително заплащане за куче',
        }

    def __init__(self, *args, **kwargs):
        super(CreateNightsPlaceForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())


class CreateEatPlaceForm(forms.ModelForm):
    class Meta:
        model = Eat
        exclude = ('approved', 'user')
        labels = {
            'name': 'Име',
            'district': 'Област',
            'city': 'Населено място',
            'latitude': 'Географска ширина',
            'longitude': 'Географска дължина',
            'description': 'Описание',
            'website': 'Уебсайт',
            'price': 'Ценови Диапазон',
            'type': 'Вид',
            'image': 'Снимка',
            'phone': 'Телефон за връзка',
        }

    def __init__(self, *args, **kwargs):
        super(CreateEatPlaceForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())


class CreateWalkPlaceForm(forms.ModelForm):
    class Meta:
        model = Walk
        exclude = ('approved', 'user')
        labels = {
            'name': 'Име',
            'district': 'Област',
            'city': 'Населено място',
            'latitude': 'Географска ширина',
            'longitude': 'Географска дължина',
            'description': 'Описание',
            'website': 'Уебсайт',
            'type': 'Категория',
            'dogs_are_welcome': 'Допускане на кучета',
            'image': 'Снимка',
            'entrance_fee': 'Такса за вход',
            'holidays': 'Почивни дни',
            'duration': 'Времетраене',
            'distance': 'Разстояние в километри',
            'displacement': 'Дениевлация в метри',
            'difficulty': 'Трудност',
            'phone': 'Телефон за връзка',
        }

    def __init__(self, *args, **kwargs):
        super(CreateWalkPlaceForm, self).__init__(*args, **kwargs)
        field_required_error(self.fields.values())
