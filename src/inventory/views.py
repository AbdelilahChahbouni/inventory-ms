from django.shortcuts import render
from .models import *
from .filters import InventoryStockFilter   
from .forms import *
from django_filters.views import FilterView
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages



class StockListView(FilterView):
    queryset = InventoryStock.objects.filter(is_deleted=False)
    filterset_class = InventoryStockFilter
    template_name = 'inventory.html'
    paginate_by = 10


