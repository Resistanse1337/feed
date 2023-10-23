from django.urls import path

from . import views

urlpatterns = [
    path("user/<int:pk>/events/", views.EventsView.as_view()),
]
