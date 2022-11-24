from django.urls import path
from . import views

urlpatterns = [
    path("transactions/upload/", views.UploadTransictionView.as_view()),
    path("transactions/", views.ListAllTransictionView.as_view()),
    path(
        "transactions/stores/<str:store>/", views.ListByStoreTransictionView.as_view()
    ),
]
