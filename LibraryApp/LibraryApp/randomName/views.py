from django.shortcuts import render

def randomName(request, name):
    return render(request, "randomName.html")