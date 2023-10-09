from django.shortcuts import render, redirect
from django.http import HttpResponse

# from django.forms import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .forms import BorrowedForm, CreateUserForm
from .filters import BorrowFilter
from .decorators import unauthenticated_user, allowed_users, admin_only

# Create your views here.


@unauthenticated_user
def registerPage(request):
    # if user is authenticated go home, else login or register
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            group = Group.objects.get(name="staff")
            user.groups.add(group)
            Staff.objects.create(
                user=user,
            )

            messages.success(request, "Account was created for " + username)

            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):
    #    if request.user.is_authenticated:
    #        return redirect('home')
    #    else:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        # make sure user is in the database
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "username OR password is incorrect")

    context = {}
    return render(request, "accounts/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


@login_required(login_url="login")
# @allowed_users(allowed_roles=['admin'])
@admin_only
def home(request):
    borrowed_items = Borrowed_items.objects.all()
    staff = Staff.objects.all()
    items = Item.objects.all()

    total_staff = staff.count()
    total_amount = sum(item.amount for item in items)

    borrowed = borrowed_items.filter(status="Borrowed").count()
    returned = borrowed_items.filter(status="Returned").count()

    context = {
        "borrowed_items": borrowed_items,
        "staff": staff,
        "items": staff,
        "total_staff": total_staff,
        "borrowed": borrowed,
        "returned": returned,
        "total_amount": total_amount,
    }

    return render(request, "accounts/dashboard.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["staff"])
def userPage(request):
    borrows = request.user.staff.borrowed_items_set.all()

    items = Item.objects.all()

    total_amount = sum(item.amount for item in items)
    borrowed = borrows.filter(status="Borrowed").count()
    returned = borrows.filter(status="Returned").count()

    context = {
        "borrows": borrows,
        "borrowed": borrowed,
        "returned": returned,
        "total_amount": total_amount,
        "items": staff,
    }

    return render(request, "accounts/user-page.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def items(request):
    items = Item.objects.all()
    return render(request, "accounts/items.html", {"items": items})


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def staff(request, pk):
    staff = Staff.objects.get(id=pk)
    borrows = staff.borrowed_items_set.all()
    total_borrowed = borrows.filter(status="Borrowed").count()

    myFilter = BorrowFilter(request.GET, queryset=borrows)
    borrows = myFilter.qs

    context = {
        "staff": staff,
        "borrows": borrows,
        "total_borrowed": total_borrowed,
        "myFilter": myFilter,
    }
    return render(request, "accounts/staff.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def createBorrow(request, pk):
    staff = Staff.objects.get(id=pk)
    form = BorrowedForm(initial={"staff": staff})
    if request.method == "POST":
        form = BorrowedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"staff": staff, "form": form}
    return render(request, "accounts/borrow_form.html", context)


@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def updateBorrow(request, pk):
    borrow = Borrowed_items.objects.get(id=pk)
    form = BorrowedForm(instance=borrow)
    if request.method == "POST":
        form = BorrowedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "accounts/borrow_form.html", context)


# if use formset the update part has problem.
@login_required(login_url="login")
@allowed_users(allowed_roles=["admin"])
def deleteBorrow(request, pk):
    borrow = Borrowed_items.objects.get(id=pk)
    if request.method == "POST":
        borrow.delete()
        return redirect("/")

    context = {"item": borrow}
    return render(request, "accounts/delete.html", context)
