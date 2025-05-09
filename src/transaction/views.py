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
    

class PurchseListView(generic.ListView):
    model = PurchaseBill
    template_name = 'purchase/purchase_list.html'
    context_object_name = 'bills'
    ordering = ['-time']
    paginate_by = 10


class SelectSupplierForm(forms.ModelForm):
    form_class = SelectSuplierForm
    template_name = 'purchase/select_supplier.html'

    def get(self ,request, *args , **kwargs):
        form = self.form_class
        return render(request , self.template_name , {'form':form})
    
    def post(self , request , *args , **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            supp_id = request.POST.get('suplier')
            supplier = get_object_or_404(Supplier , id=supp_id)
            return redirect('new_purchase' , supplier.id)
        return render(request , self.template_name , {'form':form})
    




