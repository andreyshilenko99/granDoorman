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
    context_object_name = 'event_list'
    queryset = Event.time
    template_name = 'list.html'  # Определение имени вашего шаблона и его расположения
