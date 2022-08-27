from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
# from django.contrib.auth.models import User, Group
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

# #User profiles
# def register(request):
#     print(request)
#     username = request.POST['username']
#     password = request.POST['password']
#     new_user = User.objects.create_user(username, password)
#     new_user.save()
#     HttpResponseRedirect('/index')

# def changePassword(request):
#     username = request.POST['username']
#     new_pwd = request.POST['new_password']
#     user = User.object.get(username=username)
#     user.set_password(new_pwd)
#     user.save

def loggingOut(request):
    logout(request)

def loginUser(request):
    errors = []

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password'],
        )
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            errors.append("Invalid login information!")

    return render(request, 'accounts/login.html', {'errors': errors})
    # if user is not None:
    #     login(request, user)
    #     return HttpResponse(user)
    # else:
    #     return HttpResponse(user)

# def votesView(request):
#     if request.user.is_authenticated:
#         pass

#     else:
#         pass

# def email_check(user):
#     return user.email.endswith('@email.com')

# def newAdmin(request):
#     username = request.POST['username']
#     new_admin = User.object.get(username=username)
#     group = Group.objects.get(name='admins')
#     new_admin.groups.add(group)