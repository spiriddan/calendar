from django.shortcuts import render


def calendar_view(request):
    # Add logic here to pass data to the calendar template
    return render(request, 'calendar.html')


# from django.http import HttpResponse
#
#
# def simple_view(request):
#     return HttpResponse("Hello, this is a simple view!")
