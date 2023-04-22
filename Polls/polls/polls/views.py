from django.shortcuts import render
from django.http import HttpResponse
from polls.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from polls.forms import QuestionModelForm
from django.utils import timezone


def view_Questions(request):
    Questions = Question.objects.all()
    p = Paginator(Question.objects.all(), 1)
    page = request.GET.get('page')
    Question = p.get_page(page)

    context = {
        "Questions": Questions,
        "Question": Question,
    }
    return render(request, "polls/Questions.html", context)

def view_Question(request, QuestionID):
    Question = get_object_or_404(Question, pk=QuestionID)
    context = {
        "Question": Question,
    }
    return render(request, "polls/question.html", context)

def create(request):
    if request.method == "GET":
        form = QuestionModelForm()
        context = {
            "form": form
        }
        return render(request, "polls/login.html", context)
    elif request.method == "POST":

        form = QuestionModelForm(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.pub_date = timezone.now()
            new_question.save()
            return redirect("/polls")

def delete(request, QuestionID):
    Question = Question.objects.get(id=QuestionID)
    Question.delete()
    return redirect("/polls")