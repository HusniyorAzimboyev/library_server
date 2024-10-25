from django.urls import path,include
from .views import first,pages

urlpatterns = [
    path('',first,name="first_page"),
    path('pages/<page>',pages,name="pages")
]