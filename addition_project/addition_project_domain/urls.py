from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sümüklü", views.create_category, name="create_category"),
]
