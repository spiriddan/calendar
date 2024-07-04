# urls.py in your app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='simple_view'),
]