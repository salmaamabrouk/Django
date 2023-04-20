
from django.contrib import admin
from django.urls import path, include
from LibraryApp.Hello.views import Hello
#from LibraryApp.randomName.views import randomName

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Hello/', include("LibraryApp.Hello.urls")),
    path('randomName/', include("LibraryApp.randomName.urls")),
]
