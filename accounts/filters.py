import django_filters


from .models import *

class BorrowFilter(django_filters.FilterSet):
    class Meta:
        model = Borrowed_items
        fields = '__all__'