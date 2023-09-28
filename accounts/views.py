from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('home')

def items(request):
    return HttpResponse('items')

def staff(request):
    return HttpResponse('staff')