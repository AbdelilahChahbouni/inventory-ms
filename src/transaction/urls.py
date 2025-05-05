from django.urls import path 
from .views import *



urlpatterns = [
    path('supliers_list' , SuplierListView.as_view() , name='supliers_list'),
    path('create_suplier' , CreateSuplierView.as_view() , name='create_suplier'),
]