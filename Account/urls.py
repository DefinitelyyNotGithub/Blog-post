from django.urls import path
from . import views

app_name = "Account"

urlpatterns = [
    path('login', views.LogIn_View.as_view(), name='login'),
    path('register', views.Register_View.as_view(), name='register'),
    path('logout', views.LogOut_View.as_view(), name='logout'),
    path('profile/<int:pk>', views.UserProfile.as_view(), name='profile'),
    path('saved-post', views.SavedPost.as_view(), name='saved posts'),
    path('liked-post', views.LikedPost.as_view(), name='liked posts'),
]