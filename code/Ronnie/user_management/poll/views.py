from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

## Home Page and voting
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list': latest_question_list,
        }
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    discord = request.POST['discord']
    new_user = User.objects.create_user(username, password)
    new_user.save()
    return HttpResponse("You have registered")

def logoutUser(request):
    logout(request)
    return HttpResponse("you are not logged in")

def loginUser(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if request.user is not None:
        login(request, user)
        return HttpResponse("You're logged in")
    else:
        return HttpResponse("Username and password does not match")
