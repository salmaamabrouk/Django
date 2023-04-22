from django.urls import path
from users.views import *

urlpatterns = [
    path('login', login, name = "login"),
    path('logout', logout, name = 'logout'),
]