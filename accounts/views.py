from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    borrowed_items = Borrowed_items.objects.all()
    staff = Staff.objects.all()
    items = Item.objects.all()
     
    total_staff = staff.count()
    total_items = items.count()
   
    borrowed = borrowed_items.filter(status='Borrowed').count()
    returned = borrowed_items.filter(status='Returned').count()
    
    
    context = {'borrowed_items': borrowed_items, 'staff':staff, 'items':staff, 'total_staff':total_staff, 'borrowed':borrowed,
                'returned':returned,'total_items':total_items}
    
    return render(request,'accounts/dashboard.html', context)

def items(request):
    items = Item.objects.all()
    return render(request,'accounts/items.html', {'items':items})

def staff(request,pk):
    staff = Staff.objects.get(id=pk)
    borrows = staff.borrowed_items_set.all()
    total_borrowed = borrows.filter(status='Borrowed').count()
    context = {'staff':staff, 'borrows':borrows, 'total_borrowed':total_borrowed}
    return render(request,'accounts/staff.html',context)

   