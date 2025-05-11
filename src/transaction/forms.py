from django import forms 
from .models import *
from inventory.models import InventoryStock
from django.forms import formset_factory


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name' , 'phone' , 'address' , 'gstin' , 'email']


class SelectSuplierForm(forms.ModelForm):
    def __init__(self,*args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['suplier'].queryset = Supplier.objects.filter(is_deleted=False)
        self.fields['suplier'].widget.attrs.update({'class':'textinput form-control'})
    class Meta:
        model = PurchaseBill
        fields = ['suplier']

class PurchaseItemForm(forms.ModelForm):
    def __init__(self,*args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['stock'].queryset =InventoryStock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class':'textinput form-control set_price stock', 'required':'true' })
        self.fields['quantity'].widget.attrs.update({'class':'textinput form-control set_price quantity', 'required':'true','min':'1' })
        self.fields['per_price'].widget.attrs.update({'class':'textinput form-control set_price per_price', 'required':'true','min':'1' })

    class Meta:
        model = PurchaseItem
        fields = ['stock' , 'quantity' , 'per_price']

PurchaseItemFormset = formset_factory(PurchaseItemForm , extra=1)


class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseBillDetails
        fields = ['eway', 'veh', 'destination', 'po','cgst', 'sgst', 'igst', 'cess', 'tcs']