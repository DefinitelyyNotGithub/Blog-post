from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('contact', views.ContactUs_View.as_view(), name="contact_us"),
    path('', views.Main_View.as_view(), name='main'),
    path('aboutus', views.AboutUs_View.as_view(), name="about_us"),

]