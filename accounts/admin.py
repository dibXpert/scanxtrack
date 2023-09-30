from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Staff)
admin.site.register(Item)
admin.site.register(Borrowed_items)