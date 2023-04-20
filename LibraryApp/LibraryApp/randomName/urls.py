
from django.urls import path
from LibraryApp.randomName.views import randomName

urlpatterns = [
    path('<name>', randomName),
]
