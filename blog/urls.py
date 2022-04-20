from django.urls import path
from .views import render_post, post_detail, postCreateView, postUpdateView

app_name = 'blog'

urlpatterns = [
    path('', render_post, name='posts'),
    path('<int:post_id>', post_detail, name='post_detail'),
    path('add', postCreateView.as_view(), name='post_create'),
    path('<slug>/update', postUpdateView.as_view(), name='post_update'),
]
