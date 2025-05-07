from django.urls import path 
from .views import *



urlpatterns = [
    path('supliers_list' , SuplierListView.as_view() , name='supliers_list'),
    path('create_suplier' , CreateSuplierView.as_view() , name='create_suplier'),
    path('update_suplier/<str:pk>',UpdateSuplierView.as_view(),name='update_suplier'),
    path('delete_suplier/<str:pk>',DeleteSuplierView.as_view(),name='delete_suplier')

]