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
    success_url = '/transaction/supliers_list'
    success_message = "the suplier created successfully"
    

class UpdateSuplierView(generic.UpdateView):
    model = Supplier
    template_name = 'suplier/update_suplier.html'
    form_class = SupplierForm
    success_url = '/transaction/supliers_list'
    success_message = "the suplier updated successfully"

class DeleteSuplierView(generic.View):
    def get(self,request,pk):
        suplier = get_object_or_404(Supplier , pk=pk)
        return render(request , 'suplier/delete_suplier.html' ,{'suplier':suplier})
    def post(self , request , pk):
        suplier = get_object_or_404(Supplier , pk=pk)
        suplier.is_deleted = True
        suplier.save()
        return redirect('supliers_list')



