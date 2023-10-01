from django.shortcuts import render, redirect
from django.http import HttpResponse
#from django.forms import inlineformset_factory
from .models import *
from .forms import BorrowedForm
# Create your views here.
def home(request):
    borrowed_items = Borrowed_items.objects.all()
    staff = Staff.objects.all()
    items = Item.objects.all()
     
    total_staff = staff.count()
    total_amount = sum(item.amount for item in items)
   
    borrowed = borrowed_items.filter(status='Borrowed').count()
    returned = borrowed_items.filter(status='Returned').count()
    
    
    context = {'borrowed_items': borrowed_items, 'staff':staff, 'items':staff, 'total_staff':total_staff, 'borrowed':borrowed,
                'returned':returned, 'total_amount':total_amount}
    
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

def createBorrow(request,pk):
    staff = Staff.objects.get(id=pk)
    form = BorrowedForm(initial={'staff':staff})
    if request.method == 'POST':
        form = BorrowedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'staff':staff,'form':form}
    return render(request,'accounts/borrow_form.html', context)

def updateBorrow(request, pk):
    borrow = Borrowed_items.objects.get(id=pk)
    form = BorrowedForm(instance=borrow)
    if request.method == 'POST':
        form = BorrowedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/borrow_form.html',context)

def deleteBorrow(request, pk):
    borrow = Borrowed_items.objects.get(id=pk)
    if request.method == "POST":
        borrow.delete()
        return redirect ('/')
    
    context = {'item':borrow}
    return render(request, 'accounts/delete.html', context)    

# def createBorrow(request, pk):
#     BorrowFormSet = inlineformset_factory(Staff, Borrowed_items, fields=('item', 'status'), extra=5)
#     staff = Staff.objects.get(id=pk)
#     formset = BorrowFormSet(queryset=Borrowed_items.objects.none(), instance=staff)
    
#     if request.method == 'POST':
#         formset = BorrowFormSet(request.POST, instance=staff)
#         if formset.is_valid():
#             formset.save()
#             return redirect('/')
    
#     context = {'form_or_formset': formset}
#     return render(request, 'accounts/borrow_form.html', context)

# def updateBorrow(request, pk):
#     borrowed = Borrowed_items.objects.get(id=pk)
#     form = Borrowed_items_form(instance=borrowed)
    
#     if request.method == 'POST':
#         form = Borrowed_items_form(request.POST, instance=borrowed)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
        
#     context = {'form_or_formset': form}
#     return render(request, 'accounts/borrow_form.html', context)

