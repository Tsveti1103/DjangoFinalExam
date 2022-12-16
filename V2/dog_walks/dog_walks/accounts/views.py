from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import views as auth_views, login, authenticate
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import get_user_model

from dog_walks.accounts.forms import RegisterUserForm, LoginUserForm, ProfileUpdateForm, MyPasswordChangeForm
from dog_walks.accounts.models import Profile, AppUser
from dog_walks.common.models import WalkLike, NightLike, EatLike, NightWantToVisit, EatWantToVisit, WalkWantToVisit
from dog_walks.core.utils import get_user_objects, set_paginator
from dog_walks.places.models import Walk, Night, Eat

UserModel = get_user_model()


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = MyPasswordChangeForm
    template_name = 'profile/change_password.html'
    success_message = "Успешно променихте паролата си!"
    success_url = reverse_lazy('index')


class UserRegisterView(SuccessMessageMixin, views.CreateView):
    template_name = 'profile/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')
    success_message = "Добре дошъл!"
    redirect_authenticated_user = reverse_lazy('index')

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        to_return = super().form_valid(form)
        # login(self.request, self.object)
        user = authenticate(
            username=form.cleaned_data["email"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class UserLoginView(auth_views.LoginView):
    template_name = 'profile/login.html'
    redirect_authenticated_user = reverse_lazy('index')
    form_class = LoginUserForm


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class UserDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profile/profile-details.html'
    model = AppUser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_liked_objects = len(get_user_objects([WalkLike, NightLike, EatLike], self.object.pk))
        all_created_objects = len(get_user_objects([Walk, Night, Eat], self.object.pk))
        all_want_to_visit_objects = len(
            get_user_objects([NightWantToVisit, EatWantToVisit, WalkWantToVisit], self.object.pk))
        context['all_liked_objects'] = all_liked_objects
        context['all_created_objects'] = all_created_objects
        context['all_want_to_visit_objects'] = all_want_to_visit_objects
        context['username'] = self.object.profile.username
        context['dog_name'] = self.object.profile.dog_name
        context['residence'] = self.object.profile.residence
        context['profile_image'] = self.object.profile.profile_image
        context['email'] = self.request.user.email
        return context


class UserDeleteView(LoginRequiredMixin, views.DeleteView):
    template_name = 'profile/profile-delete.html'
    model = UserModel
    success_url = reverse_lazy('index')


class UserEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profile/profile-edit.html'
    model = Profile
    form_class = ProfileUpdateForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

    def form_valid(self, form):
        profile = form.save()
        user = profile.user
        user.username = form.cleaned_data['username']
        user.profile_image = form.cleaned_data['profile_image']
        user.dog_name = form.cleaned_data['dog_name']
        user.residence = form.cleaned_data['residence']
        user.save()
        return super().form_valid(form)


def user_liked_places(request, pk):
    all_objects = get_user_objects([WalkLike, NightLike, EatLike], pk)
    places = set_paginator(request, all_objects, 2)
    context = {
        'places': places
    }
    return render(
        request,
        'profile/user_liked_places.html',
        context,
    )


def user_places(request, pk):
    all_objects = get_user_objects([Walk, Night, Eat], pk)
    places_list = [p for p in all_objects if p.approved is True]
    places = set_paginator(request, places_list, 2)

    context = {
        'places': places
    }
    return render(
        request,
        'profile/user_places.html',
        context,
    )


def user_places_wait_for_approval(request, pk):
    all_objects = get_user_objects([Walk, Night, Eat], pk)
    places_list = [p for p in all_objects if p.approved is False]
    places = set_paginator(request, places_list, 2)

    context = {
        'places': places
    }
    return render(
        request,
        'profile/user_places_for_approve.html',
        context,
    )


def user_want_to_visit_places(request, pk):
    all_objects = get_user_objects([NightWantToVisit, EatWantToVisit, WalkWantToVisit], pk)
    places = set_paginator(request, all_objects, 2)

    context = {
        'places': places
    }
    return render(
        request,
        'profile/user_want_to_visit_places.html',
        context,
    )
