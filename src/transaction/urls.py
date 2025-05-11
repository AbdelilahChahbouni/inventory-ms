from django.urls import path 
from .views import *



urlpatterns = [
    path('supliers_list' , SuplierListView.as_view() , name='supliers_list'),
    path('create_suplier' , CreateSuplierView.as_view() , name='create_suplier'),
    path('update_suplier/<str:pk>',UpdateSuplierView.as_view(),name='update_suplier'),
    path('delete_suplier/<str:pk>',DeleteSuplierView.as_view(),name='delete_suplier'),

    #Purchases

    path('purchase_list' , PurchseListView.as_view() , name='purchase_list' ),
    path('select_supplier', SelectSupplierView.as_view(), name='select_supplier'),
    path('new_purchase/<str:pk>',PurchaseCeateView.as_view(), name='new_purchase'),
    path('purchase_delete/<str:pk>',PurchaseDeleteView.as_view(), name='delete_purchase'),
    path('purchase_bill/<str:bill_no>', PurchaseBillView.as_view(), name='purchase_bill'),

]