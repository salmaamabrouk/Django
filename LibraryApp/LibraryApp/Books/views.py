from django.shortcuts import render

def hello(request, name):
    context = {
        "name": name
    }

    return render(request, "books.html", context)