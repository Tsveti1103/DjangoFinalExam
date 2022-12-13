from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils.translation import ugettext


def get_user_objects(object_models, pk):
    places_list = []
    for model in object_models:
        model_list = list(model.objects.filter(user_id=pk))
        places_list.extend(model_list)
    return places_list


def set_paginator(request, objects, count):
    page = request.GET.get('page', 1)
    paginator = Paginator(objects, count)
    try:
        obj = paginator.page(page)
    except PageNotAnInteger:
        obj = paginator.page(1)
    except EmptyPage:
        obj = paginator.page(paginator.num_pages)
    return obj


def field_required_error(fields):
    for field in fields:
        field.error_messages = {
            'required': ugettext('Полето за {fieldname} е задължително !!!').format(fieldname=field.label),
            'invalid': ugettext('Полето за {fieldname} е невалидно !!!').format(fieldname=field.label)
        }
