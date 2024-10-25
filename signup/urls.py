from django.urls import path
from .views import main_page, users_table

urlpatterns = [
    path('',main_page,name='formpage'),
    path('table/',users_table,name='table_list')
]