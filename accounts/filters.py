import django_filters
from django_filters import DateFilter


from .models import *

class BorrowFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr='gte')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')
    
    class Meta:
        model = Borrowed_items
        fields = '__all__'
        exclude = ['staff', 'date_created']