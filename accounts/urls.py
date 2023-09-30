from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('items/', views.items, name="items"),
    path('staff/<str:pk>', views.staff, name="staff"),
    path('create_borrow/', views.createBorrow, name="create_borrow")
]