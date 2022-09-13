from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name = "home"),
    path("letters/", views.letter_inbox, name = "letter_inbox"),
    path("letters/create", views.LetterCreateView.as_view(), name = "letter_create"),
    path("letters/perm/<int:pk>", views.reject_letter, name = "reject_letter"),
    # path("letters/perm/<int:pk>", views.LetterUpdateView.as_view(), name = "letter_edit"),
    # path("letters/detail/<int:pk>", views.LetterDetailView.as_view(), name = "letter_detail"),
    path("letters/detail/<int:pk>", views.message_view, name = "letter_detail"),
]


