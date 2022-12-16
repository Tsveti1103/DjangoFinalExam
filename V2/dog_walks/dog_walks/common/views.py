from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import pyperclip
from django.urls import reverse_lazy

from dog_walks.common.forms import NightsCommentForm, EatCommentForm, WalkCommentForm, NightReportForm, EatReportForm, \
    WalkReportForm, ContactUserForm
from dog_walks.common.map_utils import create_map
from dog_walks.common.models import NightLike, EatLike, WalkLike, NightWantToVisit, EatWantToVisit, WalkWantToVisit
from dog_walks.common.utils import get_place_url, user_interacts_with_obj, get_all_places


def index(request):
    context = {}
    return render(request, 'index.html', context)


class SearchResultsView(views.ListView):
    template_name = "base/search_results.html"
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get("query")
        object_list = get_all_places(query)
        return object_list


def map_page(request):
    the_map = create_map()
    the_map = the_map._repr_html_()
    context = {'the_map': the_map}
    return render(request, 'map.html', context)


@login_required
def like_night(request, pk):
    return user_interacts_with_obj(request, pk, NightLike)


@login_required
def like_eat(request, pk):
    return user_interacts_with_obj(request, pk, EatLike)


@login_required
def like_walk(request, pk):
    return user_interacts_with_obj(request, pk, WalkLike)


@login_required
def want_to_visit_night(request, pk):
    return user_interacts_with_obj(request, pk, NightWantToVisit)


@login_required
def want_to_visit_eat(request, pk):
    return user_interacts_with_obj(request, pk, EatWantToVisit)


@login_required
def want_to_visit_walk(request, pk):
    return user_interacts_with_obj(request, pk, WalkWantToVisit)


class CreateNightReportView(LoginRequiredMixin, views.CreateView):
    form_class = NightReportForm
    template_name = 'places/report_night_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details night', kwargs={'pk': place_id})

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.place_id = self.kwargs['pk']
        report.save()
        return super(CreateNightReportView, self).form_valid(form)


class CreateEatReportView(LoginRequiredMixin, views.CreateView):
    form_class = EatReportForm
    template_name = 'places/report_eat_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details eat', kwargs={'pk': place_id})

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.place_id = self.kwargs['pk']
        report.save()
        return super(CreateEatReportView, self).form_valid(form)


class CreateWalkReportView(LoginRequiredMixin, views.CreateView):
    form_class = WalkReportForm
    template_name = 'places/report_walk_place.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_pk'] = self.kwargs['pk']
        return context

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details walk', kwargs={'pk': place_id})

    def form_valid(self, form):
        report = form.save(commit=False)
        report.user = self.request.user
        report.place_id = self.kwargs['pk']
        report.save()
        return super(CreateWalkReportView, self).form_valid(form)


class CreteNightCommentView(LoginRequiredMixin, views.CreateView):
    form_class = NightsCommentForm

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details night', kwargs={'pk': place_id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.place_id = self.kwargs['pk']
        comment.save()
        return super(CreteNightCommentView, self).form_valid(form)


class CreteWalkCommentView(LoginRequiredMixin, views.CreateView):
    form_class = WalkCommentForm

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details walk', kwargs={'pk': place_id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.place_id = self.kwargs['pk']
        comment.save()
        return super(CreteWalkCommentView, self).form_valid(form)


class CreteEatCommentView(LoginRequiredMixin, views.CreateView):
    form_class = EatCommentForm

    def get_success_url(self):
        place_id = self.object.place_id
        return reverse_lazy('details eat', kwargs={'pk': place_id})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.place_id = self.kwargs['pk']
        comment.save()
        return super(CreteEatCommentView, self).form_valid(form)


@login_required
def share(request):
    current_page = get_place_url(request)
    pyperclip.copy(current_page)
    return redirect(current_page)


class AboutUs(views.TemplateView):
    template_name = 'footer/about_us.html'


class TermsAndConditions(views.TemplateView):
    template_name = 'footer/terms_and_conditions.html'


class ContactUsView(views.FormView):
    form_class = ContactUserForm
    template_name = 'footer/contact_us.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        contact = form.save(commit=False)
        if self.request.user.is_authenticated:
            contact.email = self.request.user
            form.cleaned_data['email'] = contact.email
        contact.save()
        return super(ContactUsView, self).form_valid(form)
