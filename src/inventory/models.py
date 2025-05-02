from django.db import models
import uuid
class InventoryStock(models.Model):
    id = models.AutoField(primary_key=True , default=uuid.uuid4)
    name = models.CharField(max_length=255 , unique=True)
    quantity = models.DecimalField(max_digits=10 , decimal_places=2,default=1)
    is_deleted = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True , blank=True , null=True)

    def __str__(self):
        return self.name
    

