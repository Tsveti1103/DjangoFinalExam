from django.contrib import admin

from dog_walks.common.models import NightReport, NightComment, EatComment, WalkComment, EatReport, WalkReport, ContactUs


class PlaceReportAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'place', 'description', 'publication_date_and_time']
    ordering = ('publication_date_and_time',)
    list_display = ['user', 'get_place_name', 'publication_date_and_time', 'is_checked_by_staff']
    list_filter = ('is_checked_by_staff', 'publication_date_and_time', 'user', 'place__name')

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    @admin.display(ordering='place__name', description='Place')
    def get_place_name(self, obj):
        return obj.place.name

    get_place_name.admin_order_field = 'place'
    get_place_name.short_description = 'Place Name'


@admin.register(NightReport)
class NightReportAdmin(PlaceReportAdmin):
    pass


@admin.register(EatReport)
class EatReportAdmin(PlaceReportAdmin):
    pass


@admin.register(WalkReport)
class WalkReportAdmin(PlaceReportAdmin):
    pass


class PlaceCommentAdmin(admin.ModelAdmin):
    ordering = ('publication_date_and_time',)
    list_display = ['user', 'get_place_name', 'publication_date_and_time', 'is_checked_by_staff']
    list_filter = ('publication_date_and_time', 'user', 'place__name', 'is_checked_by_staff')

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    @admin.display(ordering='place__name', description='Place')
    def get_place_name(self, obj):
        return obj.place.name

    get_place_name.admin_order_field = 'place'
    get_place_name.short_description = 'Place Name'


@admin.register(NightComment)
class NightCommentAdmin(PlaceCommentAdmin):
    pass


@admin.register(EatComment)
class EatCommentAdmin(PlaceCommentAdmin):
    pass


@admin.register(WalkComment)
class WalkCommentAdmin(PlaceCommentAdmin):
    pass


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    ordering = ('publication_date_and_time',)
    list_display = ['email', 'is_checked_by_staff', 'publication_date_and_time']
    list_filter = ('email', 'is_checked_by_staff', 'publication_date_and_time',)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False
