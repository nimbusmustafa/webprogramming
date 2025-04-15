from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic, View
from django.db.models import Q

from . import models
from .forms import SearchForm

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from .forms import CustomSignUpForm  # Assuming CustomSignUpForm is in forms.py

class SignUpView(View):
    def get(self, request):
        form = CustomSignUpForm()  # Use the signup form
        return render(request, 'registration/signin.html', {'form': form})

    def post(self, request):
        form = CustomSignUpForm(request.POST)  # Use the signup form for POST data
        if form.is_valid():  # Check if the form is valid
            user = form.save()  # Save the new user
            # Automatically log the user in after successful sign-up
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('content:index')  # Redirect to the homepage or any page you prefer
        return render(request, 'registration/signin.html', {'form': form})  # Return the form with errors if it's invalid

# Login View
class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('content:index')  # Redirect to the homepage or any page you prefer
        return render(request, 'registration/login.html', {'form': form})  # Return form with errors if invalid

# Logout View
class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('content:index')  # Redirect to the homepage or any page you prefer

class Index(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'last_blog': models.Blog.objects.order_by('-pk').filter(publish=True)[:1],
            'skills': models.Skill.objects.all(),
            'blogs': models.Blog.objects.order_by('-pk').filter(publish=True)[1:5],
            'videocasts': models.Videocast.objects.order_by('-pk').filter(publish=True)[:4]
        }
        return render(request, self.template_name, context)

class Search(View):
    template_name = 'search.html'

    def get(self, request, *args, **kwargs):
        form = SearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            context = {
                'blogs': models.Blog.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'videocasts': models.Videocast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                ),
                'podcasts': models.Podcast.objects.order_by('-pk').filter(
                    Q(title__icontains=query) | Q(content__icontains=query)
                )
            }
        else:
            return redirect('content:index')
        return render(request, self.template_name, context)


class BlogCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.BlogCategory
    fields = '__all__'
    success_message = 'Blog category was created successfully'

    def get_success_url(self):
        return reverse('content:blog_category_create')


class Blog(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'


class BlogCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Blog
    fields = '__all__'
    success_message = 'Blog was created successfully'

    def get_success_url(self):
        return reverse('content:blog_create')


class BlogArchiveByCategoryPK(generic.ListView):
    model = models.Blog
    template_name = 'blog_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category__pk=self.kwargs['pk'])

class BlogSingle(generic.DetailView):
    model = models.Blog
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class VideocastCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.VideocastCategory
    fields = '__all__'
    success_message = 'Video cast category was created successfully'

    def get_success_url(self):
        return reverse('content:videocast_category_create')


class Videocast(generic.ListView):
    model = models.Videocast
    template_name = 'videocast_archive.html'


class VideocastCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Videocast
    fields = '__all__'
    success_message = 'Video cast was created successfully'

    def get_success_url(self):
        return reverse('content:videocast_create')


class VideocastArchiveByCategoryPK(generic.ListView):
    model = models.Videocast
    template_name = 'videocast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class VideocastSingle(generic.DetailView):
    model = models.Videocast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class PodcastCategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.PodcastCategory
    fields = '__all__'
    success_message = 'Podcast category was created successfully'

    def get_success_url(self):
        return reverse('content:podcast_category_create')


class Podcast(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'


class PodcastCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Podcast
    fields = '__all__'
    success_message = 'Podcast was created successfully'

    def get_success_url(self):
        return reverse('content:podcast_create')


class PodArchiveByCategoryPK(generic.ListView):
    model = models.Podcast
    template_name = 'podcast_archive.html'

    def get_queryset(self):
        return self.model.objects.filter(category=self.kwargs['pk'])


class PodSingle(generic.DetailView):
    model = models.Podcast
    template_name = 'single.html'

    def get_queryset(self):
        return self.model.objects.filter(slug=self.kwargs['slug'])


class SkillCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    model = models.Skill
    fields = '__all__'
    success_message = 'Skill was created successfully'

    def get_success_url(self):
        return reverse('content:skill_create')
