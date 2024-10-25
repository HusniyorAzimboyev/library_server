from django.urls import path
from .views import log_in

urlpatterns = [
    path('',log_in),
]