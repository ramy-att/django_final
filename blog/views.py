#IMPORTS
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
#User can only edit their own post
# Must be logged in to post a post
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from .models import Post

#Third step for URL
#views

def home(request):
    'Displays what the user sees on the screen on the home page'
    context= {
        'posts': Post.objects.all() #uses posts created by Post class
    }
    return render(request, 'blog/home.html', context) #returns Httpresponse in back, returns html file

class PostListView(ListView):
    model=Post
    template_name='blog/home.html' #right url
    context_object_name = 'posts'
    ordering = ['-Date_Posted'] #newst post on top, oldest- bottom

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['Title', 'Content']

    def form_valid(self, form):
        form.instance.Author=self.request.user #Set author
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    fields = ['Title', 'Content']

    def form_valid(self, form):
        '''Set Author'''
        form.instance.Author=self.request.user #Set author
        return super().form_valid(form)

    def test_func(self):
        '''Only the user can edit their own post'''
        post=self.get_object()
        if self.request.user==post.Author: # author of post is logged in user
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post

    def test_func(self):
        '''Only the user can edit their own post'''
        post = self.get_object()
        if self.request.user == post.Author:  # author of post is logged in user
            return True
        return False
    success_url = '/'

def about(request):
    'Displays what the user sees on the screen on the about page'
    return render(request, 'blog/about.html', {'title':'About'})

def aboutFoot(request):
    'Displays what the user sees on the screen on the about page'
    return render(request, 'blog/aboutFoot.html', {'title':'About Football'})