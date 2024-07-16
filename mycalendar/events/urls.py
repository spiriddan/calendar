# urls.py in your app
from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendar_view, name='simple_view'),
    path('create/', views.create_event, name='create_event'),
    path('success/', views.event_success, name='event_success')
]