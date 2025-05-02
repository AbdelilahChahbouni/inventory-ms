from django.db import models

class InventoryStock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255 , unique=True)
    quantity = models.DecimalField(max_digits=10 , decimal_places=2,default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

