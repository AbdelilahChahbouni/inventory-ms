from django.db import models
import uuid
from inventory.models import InventoryStock

class Supplier(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12 , unique=True)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200 , unique=True)
    gstin = models.CharField(max_length=15 , unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class PurchaseItem(models.Model):
    bill_no = models.ForeignKey("PurchaseBill" , on_delete=models.CASCADE , related_name="purchase_bill")
    stock = models.ForeignKey(InventoryStock , on_delete=models.CASCADE , related_name="purchase_stock")
    quantity = models.IntegerField(default=1)
    per_price = models.IntegerField(default=1)
    total_price = models.IntegerField(default=1)


    def __str__(self):
        return "Bill no " + str(self.bill_no.bill_no) + "item = " + self.stock.name
    

class PurchaseBill(models.Model):
    bill_no = models.UUIDField(primary_key=True , default=uuid.uuid4)
    time = models.DateTimeField(auto_now_add=True)
    suplier = models.ForeignKey(Supplier , on_delete=models.CASCADE , related_name="purchaseBill")

    def __str__(self):
        return "Bill no " + str(self.bill_no)

    def get_total_price(self):
        purchaseItems = PurchaseItem.objects.filter(bill_no=self)
        total = 0
        for item in purchaseItems:
            total += item.total_price
        return total
    def get_items_list(self):
        return PurchaseItem.objects.filter(bill_no = self)
    
class PurchaseBillDetails(models.Model):
    bill_no = models.ForeignKey(PurchaseBill , on_delete=models.CASCADE ,related_name="purchaseBillDetail")
    eway = models.CharField(max_length=50 , blank=True , null=True )
    veh = models.CharField(max_length=50 , blank=True , null=True )
    destination = models.CharField(max_length=50 , blank=True , null=True )
    po = models.CharField(max_length=50 , blank=True , null=True )

    cgst = models.CharField(max_length=50 , blank=True , null=True )
    sgst = models.CharField(max_length=50 , blank=True , null=True )
    igst = models.CharField(max_length=50 , blank=True , null=True )
    cess = models.CharField(max_length=50 , blank=True , null=True )
    tcs = models.CharField(max_length=50 , blank=True , null=True )

    total = models.CharField(max_length=50 , blank=True , null=True )

    def __str__(self):
        return "Bill No " + str(self.bill_no.bill_no)