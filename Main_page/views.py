from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, FormView
from Blog_Post.models import Post
from .models import ContactUsModel, AboutUs_Model
from .forms import ContactUsForm
from Account.models import User


class Main_View(ListView):
    template_name = 'Main_page/index.html'
    model = Post

    def get_context_data(self, *args, **kwargs):

        context_deta = super(Main_View, self).get_context_data(*args, **kwargs)
        context_deta['article'] = Post.objects.filter(visibility=True)
        context_deta['recent_article'] = Post.objects.order_by('-spread_date')[:7]
        return context_deta


class ContactUs_View(FormView):
    template_name = 'Main_page/contact_us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('Main:main')


    def form_valid(self, form):
        data = form.cleaned_data
        user_instance = User.objects.get(email=self.request.user)
        ContactUsModel.objects.create(**data, user=user_instance)
        return super(ContactUs_View, self).form_valid(form)


class AboutUs_View(TemplateView):
    template_name = 'Main_page/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUs_View, self).get_context_data(**kwargs)
        context['obj'] = AboutUs_Model.objects.last()
        return context




