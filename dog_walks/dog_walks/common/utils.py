from django.shortcuts import redirect

from dog_walks.places.models import Night, Eat, Walk


def get_place_url(request, place_id, place_type):
    return request.META['HTTP_REFERER'] + f'#{place_type}-{place_id}'


def user_interacts_with_obj(request, pk, place_model, place_type):
    user_interacts_place = place_model.objects \
        .filter(place_id=pk, user_id=request.user.id)
    if user_interacts_place:
        user_interacts_place.delete()
    else:
        place_model.objects.create(
            place_id=pk,
            user_id=request.user.id,
        )

    return redirect(get_place_url(request, pk, place_type))


def get_all_places(query=None):
    places_list = []
    if query:
        nights = Night.objects.filter(name__contains=query)
        eats = Eat.objects.filter(name__contains=query)
        walks = Walk.objects.filter(name__contains=query)
    else:
        nights = Night.objects.all()
        eats = Eat.objects.all()
        walks = Walk.objects.all()
    places_list.extend(nights)
    places_list.extend(eats)
    places_list.extend(walks)
    return places_list

