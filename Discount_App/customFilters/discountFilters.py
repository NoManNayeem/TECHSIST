import django_filters
from ..models import Discount

class DiscountFilter(django_filters.FilterSet):
    class Meta:
        model = Discount
        fields = {
            'name': ['startswith'],
            # other filters
        }
        together = ['name',]