import datetime
import json
import time

from django.shortcuts import render
from .models import *


class Appointment:
    start = 0
    end = 0

    def __init__(self, ev: Event):
        self.start = datetime.datetime.combine(ev.day, datetime.datetime.min.time()) # datetime.date
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

        self.start = self.start.timestamp()
        self.end = self.end.timestamp()


def calendar_view(request):
    all = [Appointment(i).__dict__ for i in Event.objects.all()]

    context = {
        'events': all
    }
    # Add logic here to pass data to the calendar template
    return render(request, 'calendar.html', context=context)


# from django.http import HttpResponse
#
#
# def simple_view(request):
#     return HttpResponse("Hello, this is a simple view!")

