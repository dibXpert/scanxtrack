from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("", views.home, name="home"),
    path("items/", views.items, name="items"),
    path("staff/<str:pk>", views.staff, name="staff"),
    path("user-page/", views.userPage, name="user-page"),
    path("account/", views.accountSettings, name="account"),
    path("create_borrow/<str:pk>", views.createBorrow, name="create_borrow"),
    path("update_borrow/<str:pk>", views.updateBorrow, name="update_borrow"),
    path("delete_borrow/<str:pk>", views.deleteBorrow, name="delete_borrow"),
]
