from django.urls import path
from . import views

app_name = "Account"

urlpatterns = [
    path('login', views.LogIn_View.as_view(), name='login'),
    path('register', views.Register_View.as_view(), name='register'),
    path('logout', views.LogOut_View.as_view(), name='logout'),
]