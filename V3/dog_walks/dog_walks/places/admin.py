from django.contrib import admin

from dog_walks.places.models import Night, Eat, Walk


class BasePlaceAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'modified_date']
    list_display = ['name', 'district', 'user', 'approved']
    list_filter = ('approved', 'modified_date', 'user', 'name')

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


@admin.register(Night)
class NightAdmin(BasePlaceAdmin):
    fieldsets = (
        ("Base Place Info", {"fields": (
            'name', 'district', 'city', 'latitude', 'longitude', 'type',), },),
        ("Additional Place Info", {"fields": ('price', 'beds_count', 'image', 'dog_fee', 'description'
                                              ), },),
        ("Contacts", {"fields": ('phone', 'website',
                                 ), },),
        ("Final Info", {"fields": ('modified_date', 'user', 'approved'
                                   ), },),
    )


@admin.register(Eat)
class EatAdmin(BasePlaceAdmin):
    fieldsets = (
        ("Base Place Info", {"fields": (
            'name', 'district', 'city', 'latitude', 'longitude', 'type',), },),
        ("Additional Place Info", {"fields": ('price', 'image', 'description'
                                              ), },),
        ("Contacts", {"fields": ('phone', 'website',
                                 ), },),
        ("Final Info", {"fields": ('modified_date', 'user', 'approved'
                                   ), },),
    )


@admin.register(Walk)
class WalkAdmin(BasePlaceAdmin):
    fieldsets = (
        ("Base Place Info", {"fields": (
            'name', 'district', 'city', 'latitude', 'longitude', 'type',), },),
        ("Additional Place Info", {"fields": (
            'dogs_are_welcome', 'image', 'entrance_fee', 'description', 'holidays',
        ), },),
        ("Terrain Features", {"fields": ('duration', 'distance', 'displacement', 'difficulty',
                                         ), },),
        ("Contacts", {"fields": ('phone', 'website',
                                 ), },),
        ("Final Info", {"fields": ('modified_date', 'user', 'approved'
                                   ), },),
    )
