from django.urls import path

from events import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
]