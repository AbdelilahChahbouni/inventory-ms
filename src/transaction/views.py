from django.shortcuts import render , redirect , get_object_or_404
from .forms import *
from .models import *
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic


class SuplierListView(generic.ListView):
    queryset = Supplier.objects.filter(is_deleted=False)
    template_name = "suplier/list_supliers.html"
    paginate_by = 10


class CreateSuplierView(generic.CreateView):
    model = Supplier
    template_name = 'suplier/create_suplier.html'
    form_class = SupplierForm
    success_url = 'transaction/supliers_list'
    success_message = "the suplier created successfully"
    





