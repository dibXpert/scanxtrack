from django.forms import ModelForm
from .models import Borrowed_items

class BorrowedForm(ModelForm):
    class Meta:
        model = Borrowed_items
        fields = "__all__"