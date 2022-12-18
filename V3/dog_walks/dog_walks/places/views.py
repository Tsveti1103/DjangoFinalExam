from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from dog_walks.common.forms import NightsCommentForm, EatCommentForm, WalkCommentForm
from dog_walks.places.forms import CreateNightsPlaceForm, CreateEatPlaceForm, \
    CreateWalkPlaceForm
from django.views import generic as views
from django.urls import reverse_lazy

from dog_walks.places.models import Night, Eat, Walk
from dog_walks.places.utils import get_pacinator

UserModel = get_user_model()


class CretePlaceToEatView(SuccessMessageMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'places/create_place_to_eat.html'
    form_class = CreateEatPlaceForm
    success_url = reverse_lazy('index')
    success_message = "Мястот е създадено успешно"

    def form_valid(self, form):
        eat = form.save(commit=False)
        eat.user = self.request.user
        eat.save()
        return super(CretePlaceToEatView, self).form_valid(form)


class CretePlaceToSleepView(SuccessMessageMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'places/create_place_to_sleep.html'
    form_class = CreateNightsPlaceForm
    success_url = reverse_lazy('index')
    success_message = "Мястот е създадено успешно"

    def form_valid(self, form):
        night = form.save(commit=False)
        night.user = self.request.user
        night.save()
        return super(CretePlaceToSleepView, self).form_valid(form)


class CretePlaceToWalkView(SuccessMessageMixin, LoginRequiredMixin, views.CreateView):
    template_name = 'places/create_place_to_walk.html'
    form_class = CreateWalkPlaceForm
    success_url = reverse_lazy('index')
    success_message = "Мястот е създадено успешно"

    def form_valid(self, form):
        walk = form.save(commit=False)
        walk.user = self.request.user
        walk.save()
        return super(CretePlaceToWalkView, self).form_valid(form)


class SleepPlacesListView(views.ListView):
    model = Night
    template_name = 'places/places_to_sleep.html'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super(SleepPlacesListView, self).get_queryset()
        qs = qs.filter(approved=True).order_by("-pk")
        return qs


class EatPlacesListView(views.ListView):
    model = Eat
    template_name = 'places/places_to_eat.html'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super(EatPlacesListView, self).get_queryset()
        qs = qs.filter(approved=True).order_by("-id")
        return qs


class WalkPlacesListView(views.ListView):
    model = Walk
    template_name = 'places/places_to_walk.html'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        qs = super(WalkPlacesListView, self).get_queryset()
        qs = qs.filter(approved=True).order_by("-id")
        return qs


class NightDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'places/night_details.html'
    model = Night
    comments_paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = self.object.nightlike_set.all()
        user_like_place = likes.filter(user=self.request.user)
        want_to_visit = self.object.nightwanttovisit_set.all()
        user_want_to_visit_place = want_to_visit.filter(user=self.request.user)
        context['comment_form'] = NightsCommentForm()
        context['likes_count'] = self.object.nightlike_set.count()
        context['is_user_liked_night'] = user_like_place
        context['is_user_want_to_visit_place'] = user_want_to_visit_place
        context['is_owner'] = self.request.user == self.object.user
        context['comments'] = get_pacinator(self.request, self.object.nightcomment_set, 2, '-publication_date_and_time')
        return context


class EatDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'places/eat_details.html'
    model = Eat

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = self.object.eatlike_set.all()
        user_like_place = likes.filter(user=self.request.user)
        want_to_visit = self.object.eatwanttovisit_set.all()
        user_want_to_visit_place = want_to_visit.filter(user=self.request.user)
        context['comment_form'] = EatCommentForm()
        context['likes_count'] = self.object.eatlike_set.count()
        context['is_user_liked_eat'] = user_like_place
        context['is_user_want_to_visit_place'] = user_want_to_visit_place
        context['is_owner'] = self.request.user == self.object.user
        context['comments'] = get_pacinator(self.request, self.object.eatcomment_set, 2, '-publication_date_and_time')
        return context


class WalkDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'places/walk_details.html'
    model = Walk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes = self.object.walklike_set.all()
        user_like_place = likes.filter(user=self.request.user)
        want_to_visit = self.object.walkwanttovisit_set.all()
        user_want_to_visit_place = want_to_visit.filter(user=self.request.user)
        context['comment_form'] = WalkCommentForm()
        context['likes_count'] = self.object.walklike_set.count()
        context['is_user_liked_walk'] = user_like_place
        context['is_user_want_to_visit_place'] = user_want_to_visit_place
        context['is_owner'] = self.request.user == self.object.user
        context['comments'] = get_pacinator(self.request, self.object.walkcomment_set, 2, '-publication_date_and_time')
        return context


class NightEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'places/night-edit.html'
    fields = ['name', 'district', 'city', 'type', 'price', 'latitude', 'longitude', 'image', 'description', 'phone',
              'website']
    model = Night

    def get_success_url(self):
        return reverse_lazy('all places to sleep', )

    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)


class EatEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'places/eat-edit.html'
    fields = ['name', 'district', 'city', 'type', 'price', 'latitude', 'longitude', 'image', 'description', 'phone',
              'website']
    model = Eat

    def get_success_url(self):
        return reverse_lazy('all places to eat', )

    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)


class WalkEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'places/walk-edit.html'
    fields = ['name', 'district', 'city', 'type', 'latitude', 'longitude', 'image', 'description', 'dogs_are_welcome',
              'entrance_fee', 'open_on_weekends', 'open_on_national', 'duration', 'distance', 'displacement',
              'difficulty', 'phone', 'website']
    model = Walk

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })

    def form_valid(self, form):
        form.instance.approved = False
        return super().form_valid(form)
