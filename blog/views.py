from django.shortcuts import render, get_object_or_404
from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import Post_Create
from .models import Post, Autor 

def render_post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        posteo_form = Post_Create(request.POST)

        if posteo_form.is_valid():
            data = posteo_form.cleaned_data

        Post.objects.create(
            title = data['title'],
            autor = data['autor'],
            description = data['description'],
            content = data['content'],
            image = data['image'],
            date_posted = data['date_posted'],
            status = data['status'],
            slug = data['slug'],
        )
        return redirect('blog:posts')
    else:
        posteo_form = Post_Create()
        
        return render(request, 'post_create.html', {'posteo_form': posteo_form})

class postCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('blog:posts')
    fields = ('title', 'autor', 'description', 'content', 'image', 'date_posted', 'status', 'slug')
    template_name = "post_create.html"

class postUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('blog:posts')
    fields = ('title', 'autor', 'description', 'content', 'image', 'date_posted', 'status', 'slug')
    template_name = "post_update.html"