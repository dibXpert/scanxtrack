from django.forms import ModelForm
from .models import Borrowed_items

class Borrowed_items_form(ModelForm):
    class Meta:
        model = Borrowed_items
        fields = "__all__"