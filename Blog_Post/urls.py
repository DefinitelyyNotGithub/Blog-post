from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path('like/<slug:pk>', views.LikePost, name='like_func'),
    path('add-bookmark/<slug:pk>', views.BookMarkPost, name='bookmark_func'),
    path('list', views.postListView.as_view(), name="posts"),
    path('search', views.SideBarSearch.as_view(), name="search"),
    path('detail/<slug:pk>', views._PostDetail_.as_view(), name="post_details"),
    path('category/<int:pk>', views.Article_List_View.as_view(), name="category_list"),
    path('tag/<slug:tag_slug>', views.TagView.as_view(), name="tag"),

]
