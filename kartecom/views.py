import views as views
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
from django.views import View

from kartecom.forms import NewUserForm, NewToDoForm
from kartecom.models import Session, Idea


def index(request):
    try:
        ideas = Idea.objects.filter(user=request.user, finished=False)
        context = {
            'ideas': ideas
        }
        return render(request, 'kartecom/index.html', context)
    except:
        messages.info(request, 'No active ideas')
    return render(request, 'kartecom/index.html')


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'registration success')
            return redirect('index')
        messages.error(request, 'invalid registration information')
    form = NewUserForm()
    return render(request, 'kartecom/register.html', context={"register_form": form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                print(f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "kartecom/login.html", context={"login_form": form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')


class todo_create(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        form = NewToDoForm()
        return render(self.request, "kartecom/todo.html", context={"todo_form": form})

    def post(self, *args, **kwargs):
        form = NewToDoForm(self.request.POST)
        if form.is_valid():
            todo = Session(user=self.request.user, title=form.cleaned_data.get('title'),
                           finished=form.cleaned_data.get('finished'))
            todo.save()
        return render(self.request, "kartecom/todo.html", context={"todo_form": form})
