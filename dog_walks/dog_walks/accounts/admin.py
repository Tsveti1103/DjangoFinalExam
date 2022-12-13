from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model
from dog_walks.accounts.forms import ProfileUpdateForm, RegisterUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class AppUserAdmin(auth_admin.UserAdmin):
    form = ProfileUpdateForm
    add_form = RegisterUserForm
    fieldsets = (
        ('Personal info', {'fields': ('email',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )
    add_fieldsets = (
        ("Register", {"fields": ('email', 'password1', 'password2'), },),
    )
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser or (request.user.is_staff and request.user.groups.filter(name='HR').exists()):
            return True
        else:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser or (request.user.is_staff and request.user.groups.filter(name='HR').exists()):
            return qs
        else:
            return qs.filter(is_staff=False)
