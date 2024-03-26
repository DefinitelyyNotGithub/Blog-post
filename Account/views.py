from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views import View
from .models import User
from .forms import LogInForm, RegisterForm
from django.urls import reverse


class LogIn_View(View):

    def get(self, request):
        global second_url
        second_url = request.GET.get('next')
        form = LogInForm(request.GET)
        if not request.user.is_authenticated:
            return render(request, 'Account/Login.html', {'form': form})
        else:
            return redirect('/')

    def post(self, request):

        form = LogInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                if second_url:
                    return redirect(second_url)
                else:
                    return redirect('/')

            else:
                form.add_error('__all__', "username or password is wrong")
        return render(request, 'Account/Login.html', {'form': form})


class LogOut_View(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('/')


class Register_View(View):

    def get(self, request):
        form = RegisterForm(request.GET)
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, "Account/register.html", {"form": form})

    def post(self, request):
        second_url = request.GET.get('second_url')
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.cleaned_data.get("username"),
                                     password=form.cleaned_data.get("password"))
            login(request, user)
            if second_url:
                return redirect(second_url)
            else:
                return redirect('/')

        else:
            RegisterForm()
        return render(request, 'Account/register.html', {"form": form})
