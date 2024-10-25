from django.urls import path,include
from .views import main

urlpatterns = [
    path('',main,name="main"),
    path('library/',include("library.urls"),name="library"),
    path('new/',include("new_app.urls")),
]