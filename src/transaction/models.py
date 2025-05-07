from django.db import models
import uuid

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



