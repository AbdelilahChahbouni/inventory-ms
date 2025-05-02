from .models import *
import django_filters


class InventoryStockFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = InventoryStock
        fields = ['name']