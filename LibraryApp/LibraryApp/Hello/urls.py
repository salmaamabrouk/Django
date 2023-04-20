
from django.urls import path
from LibraryApp.Hello.views import Hello

urlpatterns = [
    path('Hello', Hello),
]
