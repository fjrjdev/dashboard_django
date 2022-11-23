from django.urls import path
from . import views

urlpatterns = [
    path("transactions/", views.ListCreateTransictionView.as_view()),
]
