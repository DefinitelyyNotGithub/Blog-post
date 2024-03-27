from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView, ListView

from Blog_Post.models import Post
from .models import User
from .forms import LogInForm, RegisterForm
from django.urls import reverse, reverse_lazy
from utils.bookmark_add_to_account import add_bookmarks_to_account


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
                add_bookmarks_to_account(request)
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
            add_bookmarks_to_account(request)
            if second_url:
                return redirect(second_url)
            else:
                return redirect('/')

        else:
            RegisterForm()
        return render(request, 'Account/register.html', {"form": form})


class UserProfile(UpdateView):

    template_name = 'Account/profile.html'
    model = User
    fields = ('full_name', 'email')
    success_url = reverse_lazy('Main:main')

    def get_context_data(self, **kwargs):
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

class SavedPost(ListView):
    template_name = 'Blog_Post/posts.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return user.bookmarked.all()

class LikedPost(ListView):
    template_name = 'Blog_Post/posts.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return user.likes.all()