from django.urls import path

from main import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories-list'),
    path('posts/', views.PostView.as_view(), name='posts-lists'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'), # можно смотреть post по id --/posts/2/--
    path('posts-update/<int:pk>/', views.PostUpdateView.as_view(), name='post-detail'),
    path('posts-delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-detail'), 


]