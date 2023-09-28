from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('items/', views.items),
    path('staff/', views.staff),
]