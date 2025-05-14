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


class SelectSupplierView(generic.View):
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
    

class PurchaseCeateView(generic.View):
    template_name = 'purchase/new_purchase.html'

    def get(self,request ,pk ):
        formset = PurchaseItemFormset(request.GET or None)
        supp_id = get_object_or_404(Supplier , pk=pk)
        context = {
            'formset' : formset,
            'supp_id' : supp_id
        }
        return render(request , self.template_name , context)
    
    def post(self , request , pk):
        formset = PurchaseItemFormset(request.POST)
        supp_id = get_object_or_404(Supplier , pk=pk)
        if formset.is_valid():
            #create Bill
            bill_obj = PurchaseBill(suplier=supp_id)
            bill_obj.save()

            #create BillDetails
            bill_obj_details = PurchaseBillDetails(bill_no=bill_obj)
            bill_obj_details.save()
            for form in formset:
                bill_item = form.save(commit=False)
                bill_item.bill_no = bill_obj
                stock = get_object_or_404(InventoryStock , name=bill_item.stock.name)
                bill_item.total_price = bill_item.per_price * bill_item.quantity
                stock.quantity += bill_item.quantity
                stock.save()
                bill_item.save()
            messages.success(request , "Purchase Items have been registred succssfuly ")
            return redirect('purchase_bill', bill_no=bill_obj.bill_no)
            # return redirect('/')
        formset = PurchaseItemFormset(request.GET or None)
        context = {
            'formset' : formset,
            'supp_id' : supp_id
        }

        return render(request , self.template_name , context)

class PurchaseDeleteView(SuccessMessageMixin , generic.DeleteView):
    model = PurchaseBill
    template_name = 'purchase/purchase_delete.html'
    success_url = '/transaction/purchase_list'

    def delete(self , *args , **kwargs):
        self.object = self.get_object()
        items = PurchaseBill.objects.filter(bill_no=self.object.bill_no)
        for item in items:
            stock = get_object_or_404(InventoryStock , name=item.stock.name)
            if stock.is_deleted == False:
                stock.quantity -= item.quantity
                stock.save()
        messages.success(self.request , "Purchase Bill Has Been Succssfuly Deleted")
        return super(PurchaseDeleteView, self).delete(*args , **kwargs)
    


class PurchaseBillView(generic.View):
    model = PurchaseBill
    template_name = 'bill/purchase_bill.html'
    bill_base = 'bill/bill_base.html'
    form_class = PurchaseDetailsForm

    def get_bill_context(self , bill_no ,form):
        bill = get_object_or_404(PurchaseBill , bill_no=bill_no)
        items = PurchaseItem.objects.filter(bill_no=bill_no)
        bill_details = get_object_or_404(PurchaseBillDetails , bill_no=bill_no)

        return {
            'bill':bill,
            'items':items,
            'bill_details':bill_details,
            'bill_base':self.bill_base,
            'form':form,
        }
    
    def get(self , request , bill_no):
        bill_details_obj = get_object_or_404(PurchaseBillDetails , bill_no=bill_no)
        form = self.form_class(instance=bill_details_obj)
        context = self.get_bill_context(bill_no=bill_no , form=form)
        return render(request , self.template_name , context)
    
    def post(self , request , bill_no):
        bill_details_obj = get_object_or_404(PurchaseBillDetails , bill_no=bill_no)
        form = self.form_class(request.POST , instance=bill_details_obj)

        if form.is_valid():
            form.save()
            messages.success(request , "Bill details have been successfuly modefied")
        else:
            messages.success(request , "There was an error updating the bill details")
        context = self.get_bill_context(bill_no , form)
        return render(request , self.template_name , context)
    




