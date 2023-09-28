from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')

def items(request):
    return render(request,'accounts/items.html')

def staff(request):
    return render(request,'accounts/staff.html')