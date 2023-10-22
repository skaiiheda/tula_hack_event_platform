from django.forms import TextInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Events
from recommendations.models import UserPreferences


def index(request):
    return render(request, 'recommendations/index.html')


class UnloggedEventsListView(ListView):
    template_name = "recommendations/index.html"
    context_object_name = 'objects'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            events = Events.objects.all()
            events_dict = {}
            for event in events:
                events_dict.setdefault(event, 0)
                for category in event.categories.all():
                    try:
                        preference = UserPreferences.objects.get(profile=user.profile, category=category)
                    except:
                        preference = None
                    if preference:
                        events_dict[event] += preference.interest_coef
            events_sorted = dict(sorted(events_dict.items(), key=lambda item: item[1])).keys()
            return events_sorted
        else:
            return Events.objects.all()[:6]


def logged_events(request):
    user = request.user
    interests = UserPreferences.objects.filter(profile=user.profile)
    events = Events.objects.all()
    events_dict = {}.setdefault(0)
    for event in events:
        for category in event.categories.all():
            preference = UserPreferences.objects.get(user=user, category=category)
            if preference:
                events_dict[event] += UserPreferences.objects.get(user=user, category=category).interest_coef
    events_sorted = [*dict(sorted(events_dict.items(), key=lambda item: item[1])).keys()]
    print(events_sorted)
    return render(request, "recommendations/index.html", {'objects': events_sorted})


@login_required
class LoggedEventsListView(ListView):
    template_name = "recommendations/index.html"
    context_object_name = 'objects'

    def get_context_data(self):
        user = self.request.user
        interests = UserPreferences.objects.filter(profile=user.profile)
        self.events = get_object_or_404(Events, name=self.kwargs["events"])
        events = Events.objects.all()
        events_dict = {}.setdefault(0)
        for event in events:
            for category in event.categories.all():
                preference = UserPreferences.objects.get(user=user, category=category)
                if preference:
                    events_dict[event] += UserPreferences.objects.get(user=user, category=category).interest_coef
        events_sorted = dict(sorted(events_dict.items(), key=lambda item: item[1])).keys()

        return events_sorted


class EventDetailView(DetailView):
    model = Events
    template_name = "recommendations/details.html"

    def get_object(self, *args, **kwargs):
        obj = super().get_object()
        obj.save()
        return obj


class EventCreateView(CreateView):
    model = Events
    fields = ['title', 'city', 'location', 'date', 'end_reg', 'categories', 'description', 'image', 'organizer']
    template_name = 'recommendations/create-event.html'

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['organizer'].widget = TextInput(attrs={'style': 'display: none;', 'value': self.request.user.organizerprofile.organization})
        return form


class EventUpdateView(UpdateView):
    model = Events
    fields = ['title', 'city', 'location', 'date', 'end_reg', 'categories', 'description', 'image', 'organizer']
    template_name_suffix = '_update_form'


class EventDeleteView(DeleteView):
    model = Events
    success_url = reverse_lazy('event-list')


def register_to_event(request, pk):
    profile = request.user.participantprofile
    event = Events.objects.get(pk=pk)
    profile.events.add(event)
    print(profile.events.all())
    return HttpResponseRedirect(f'/event/{pk}')
