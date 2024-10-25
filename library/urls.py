from django.urls import path
from .views import main,author_books,genre_books,just

urlpatterns = [
    path("",main,name="main"),
    path("books/author/<author>",author_books),
    path("books/genre/<genre>",genre_books),
    path("just/",just),
]