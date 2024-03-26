import json
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView, FormView
from .models import Post, Category, UserComments
from .forms import UserCommentForm
from django.urls import reverse_lazy


class postListView(ListView):
    template_name = 'Blog_Post/posts.html'
    model = Post
    context_object_name = 'post'
    paginate_by = 1

    def get_queryset(self):
        return Post.objects.filter(visibility=True)


class _PostDetail_(CreateView):
    model = Post
    form_class = UserCommentForm
    template_name = 'Blog_Post/index.html'

    def get_context_data(self, **kwargs):
        context = super(_PostDetail_, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug=self.kwargs[str('pk')])
        context['request'] = self.request
        return context

    def form_valid(self, form, **kwargs):
        reply = self.request.POST.get('comment_id')
        comment = form.save(commit=False)
        comment.post = Post.objects.get(slug=self.kwargs.get('pk'))
        comment.autor = self.request.user
        if reply:
            comment.parent = UserComments.objects.get(id=reply)
        comment.save()
        return redirect('post:post_details', self.kwargs.get('pk'))


class SideBarSearch(ListView):
    template_name = 'Blog_Post/posts.html'
    model = Post
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super(SideBarSearch, self).get_context_data(**kwargs)
        context['post'] = Post.objects.filter(title__icontains=self.request.GET.get('q'))
        return context


class Article_List_View(ListView):
    template_name = 'Blog_Post/posts.html'
    model = Category

    def get_context_data(self, **kwargs):
        context_date = super(Article_List_View, self).get_context_data(**kwargs)
        cat = get_object_or_404(Category, id=self.kwargs['pk'])
        context_date['post'] = cat.posts.all()
        return context_date


class TagView(ListView):
    template_name = 'Blog_Post/posts.html'
    context_object_name = 'post'
    paginate_by = 16

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs.get('tag_slug'))


def LikePost(request, pk):
    user = request.user
    post = Post.objects.get(slug=pk)

    if user in post.like.all():
        post.like.remove(user)
    else:
        post.like.add(user)
    post.save()

    return redirect('post:post_details', pk)


def BookMarkPost(request, pk):
    post = Post.objects.get(slug=pk)
    user = request.user

    if not user.is_authenticated:
        if 'saved' in request.session:
            print(request.session['saved'])
            if post.id in request.session['saved']:
                request.session['saved'].remove(post.id)
                request.session.save()
            else:
                request.session['saved'].append(post.id)
                request.session.save()
        else:
            request.session['saved'] = []
            request.session['saved'].append(post.id)
            request.session.save()

    else:
        if user in post.BookMarks.all():
            post.BookMarks.remove(user)
        else:
            post.BookMarks.add(user)

    return redirect('post:post_details', pk)
