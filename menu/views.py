from django.shortcuts import render
from django.views import generic
from .models import Event


def index(request):
    num = Event.objects.all().count()
    return render(
        request,
        'base.html',
        context={'nums': num},
    )


class EventListView(generic.ListView):
    model = Event
