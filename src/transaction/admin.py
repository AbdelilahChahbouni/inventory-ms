from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register([Supplier , PurchaseItem , PurchaseBillDetails , PurchaseBill , SaleBill , SaleItem , SaleBillDetail])

