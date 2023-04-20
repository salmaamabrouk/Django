from django.contrib import admin
from django.urls import path
from authors.views import *

urlpatterns = [

    path('', Authors),
    path('<name>', view_author),
    path('JKRowling/HarryPotter', view_harrypotter),

]