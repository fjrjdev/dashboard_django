from django.urls import path
from . import views

urlpatterns = [
    path("transactions/upload/", views.UploadTransictionView.as_view()),
    path("transactions/", views.ListCreateTransictionView.as_view()),
]
