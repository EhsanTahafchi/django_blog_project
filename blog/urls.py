from django.contrib import admin
from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='posts_list_view'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail_view'),
    path('create/', PostCreateView.as_view(), name='post_create_view'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post_update_view'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete_view'),

]
