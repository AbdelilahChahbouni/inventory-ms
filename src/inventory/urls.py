from django.urls import path
from .views import *

urlpatterns = [
    path('stock_list', StockListView.as_view(),name="stock_list"),
    path('create_stock',StockCreateView.as_view(),name="create_stock"),
    path('update_stock/<int:pk>',StockUpdateView.as_view(),name="update_stock"),
    path('delete_stock/<int:pk>',StockDeleteView.as_view(),name="delete_stock"),
]
