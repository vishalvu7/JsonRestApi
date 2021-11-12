from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('save_as_json/',views.SavedJson.as_view()),
]

