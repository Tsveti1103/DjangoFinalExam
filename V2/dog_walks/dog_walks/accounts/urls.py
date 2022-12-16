from django.urls import path, include

from dog_walks.accounts.views import UserRegisterView, UserLoginView, UserLogoutView, UserDetailsView, UserEditView, \
    UserDeleteView, user_places, user_places_wait_for_approval, user_liked_places, user_want_to_visit_places, \
    ChangePasswordView

urlpatterns = (
    path('login/', UserLoginView.as_view(), name='login user'),
    path('register/', UserRegisterView.as_view(), name='register user'),
    path('logout/', UserLogoutView.as_view(), name='logout user'),
    path('password-change/', ChangePasswordView.as_view(), name='password change'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='details user'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
        path('myplaces/', user_places, name='user places'),
        path('myplacesforapproval/', user_places_wait_for_approval, name='user places for approval'),
        path('liked_places/', user_liked_places, name='user liked places'),
        path('want_to_visit_places/', user_want_to_visit_places, name='user want to visit places'),
    ])),
)
# from .signals import *
