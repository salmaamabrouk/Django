from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect("/polls")

        else:
            messages.success(
                request, ("Login failed !"))
            return redirect("/users/login")
    else:
        return render(request, "users/login.html", {})

def logout_user(request):
    logout(request)
    messages.success(
        request, ("You are logged out !")
    )
    return redirect('/users/login')