from django.urls import path
from polls.polls import views

urlpatterns = [
    path('',views.view_Questions),
    path('<int:QuestionID>', views.view_Question, name = "question_content"),
    path('create', views.create),
    path('delete/<QuestionID>', views.delete, name = "delete"),
    ]