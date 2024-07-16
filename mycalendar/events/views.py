import datetime
from .mail import send_email_gmail, SUBJECT, BODY, TO_EMAIL, FROM_EMAIL, PASSWORD
from .models import *
from django.shortcuts import render, redirect
from .forms import EventForm
import re
from .utils import form_validation


class Appointment:
    start = 0
    end = 0
    title = ''

    def __init__(self, ev: Event):
        self.start = datetime.datetime.combine(ev.day, datetime.datetime.min.time())  # datetime.date
        if ev.is_marked_10:
            self.start += datetime.timedelta(hours=10)
        elif ev.is_marked_11:
            self.start += datetime.timedelta(hours=11)
        elif ev.is_marked_12:
            self.start += datetime.timedelta(hours=12)
        elif ev.is_marked_13:
            self.start += datetime.timedelta(hours=13)
        if ev.is_marked_14:
            self.start += datetime.timedelta(hours=14)
        elif ev.is_marked_16:
            self.start += datetime.timedelta(hours=16)
        self.end = self.start + datetime.timedelta(hours=1)

        self.title = f'{self.start.time().strftime("%H:%M")} - {self.end.time().strftime("%H:%M")}'
        self.start = self.start.timestamp()
        self.end = self.end.timestamp()


def calendar_view(request):
    all = [Appointment(i).__dict__ for i in Event.objects.all()]

    context = {
        'events': all
    }
    # Add logic here to pass data to the calendar template
    return render(request, 'calendar.html', context=context)


def create_event(request):
    exists = ''
    if request.method == 'POST':
        day = request.GET.get('day')

        extracted_date = re.search(r'[A-Z][a-z]{2} [A-Z][a-z]{2} \d{2} \d{4}', day).group()
        date_format = "%a %b %d %Y"
        dt = datetime.datetime.strptime(extracted_date, date_format).strftime('%Y-%m-%d')
        form = EventForm(request.POST)
        if form.is_valid():
            form.instance.day = dt
            if form_validation(form):
                form.save()
                send_email_gmail(SUBJECT, BODY, TO_EMAIL, FROM_EMAIL, PASSWORD)
                return redirect('event_success')
            else:
                exists = 'Такая запись уже существует'
                form = EventForm()
    else:
        form = EventForm()
    return render(request, 'create_event.html', {'form': form, 'exists': exists})


def event_success(request):
    all = [Appointment(i).__dict__ for i in Event.objects.all()]

    context = {
        'events': all
    }
    # Add logic here to pass data to the calendar template
    return render(request, 'calendar.html', context=context)
