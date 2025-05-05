from django.shortcuts import render , redirect , get_object_or_404
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
    template_name = 'inventory/inventory.html'
    # context_object_name='stocks '
    paginate_by = 10

class StockCreateView(SuccessMessageMixin, generic.CreateView):
    model = InventoryStock
    template_name = 'inventory/create_stock.html'
    form_class = InventoryStockForm
    success_url = '/'
    success_message = "Stock Created Succssefully"
    


class StockUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = InventoryStock
    template_name = 'inventory/update_stock.html'
    form_class = InventoryStockForm
    success_url = '/inventory/stock_list'
    success_message = "Stock Updated Succssefully"
    

class StockDeleteView(generic.View):
    template_name = 'inventory/delete_stock.html'
    success_message = "Stock delted Successfully"

    def get(self , request , pk):
        stock = get_object_or_404(InventoryStock , pk=pk)
        return render(request , self.template_name , {'stock':stock})
    def post(self,request,pk):
        stock = get_object_or_404(InventoryStock , pk=pk)
        stock.is_deleted = True
        stock.save()
        messages.success(request, self.success_message)
        return redirect('stock_list')
