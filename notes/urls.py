from django.urls import path
from . import views

urlpatterns = [
    path("notes", views.list),
    path("notes/<int:pl>", views.detail),
]