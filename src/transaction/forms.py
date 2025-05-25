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
        fields = ['eway', 'veh', 'destination', 'po','cgst', 'sgst', 'igst', 'cess', 'tcs','total']


class SaleForm(forms.ModelForm):
    def __init__(self , *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['name'].widget.attrs.update({'class':'textinput form-control','pattern':'[a-zA-Z\s]{1,50}','title':'Alphabets and Spaces' })
        self.fields['phone'].widget.attrs.update({'class':'textinput form-control','maxlength':'10','pattern':'[0-9]{10}','title':'Numbers' })
        self.fields['email'].widget.attrs.update({'class':'textinput form-control'})
        self.fields['gstin'].widget.attrs.update({'class':'textinput form-control','maxlength':'15','pattern':'[A-Z0-9]{15}','title':'GSTIN' })

    class Meta:
        model = SaleBill
        fields = ['name' , 'phone' , 'email' , 'gstin' , 'address']

        widgets = {
            'address': forms.Textarea(
                attrs ={
                    'class':'textinput form-control',
                    'rows':'4'
                }
            )
        }


class SaleItemForm(forms.ModelForm):
    def __init__(self , *args ,  **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['stock'].queryset = InventoryStock.objects.filter(is_deleted=False)
        self.fields['stock'].widget.attrs.update({'class':'textinput form-control set_price stock', 'required':'true' })
        self.fields['quantity'].widget.attrs.update({'class':'textinput form-control set_price quantity', 'required':'true','min':'0' })
        self.fields['per_price'].widget.attrs.update({'class':'textinput form-control set_price per_price', 'required':'true','min':'0' })

    class Meta:
        model = SaleItem
        fields = ['stock' , 'quantity', 'per_price']



SaleItemFormset = formset_factory(SaleItemForm , extra=1)

class SaleDetailForm(forms.ModelForm):
    class Meta:
        model = SaleBillDetail
        fields = ['eway', 'veh', 'destination', 'po','cgst', 'sgst', 'igst', 'cess', 'tcs','total']
