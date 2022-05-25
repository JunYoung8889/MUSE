from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    ProfileForm,
)
from django.contrib.auth.decorators import login_required
from .models import Profile


# Create your views here.
@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        form = CustomAuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@require_safe
def profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    context = {
        'person' : person,
    }
    return render(request, 'accounts/profile.html', context)


@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        if person != user:
            if user in person.followers.all():
                person.followers.remove(user)
            else:
                person.followers.add(user)
    return redirect('accounts:profile', person.pk)


@login_required
@require_http_methods(['GET', 'POST'])
def create_profile(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk) 
    if request.user == person:
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('accounts:profile', user_pk)
        else:
            form = ProfileForm()
        context = {
            'form' : form,
        }
        return render(request, 'accounts/create_profile.html', context)
    else:
        return redirect('accounts:profile', user_pk)


@login_required
@require_http_methods(['GET', 'POST'])
def update_profile(request, user_pk, profile_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user == person:
        profile = Profile.objects.get(pk=profile_pk)
        if profile == None:
            return redirect('accounts:create_profile', user_pk)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile', user_pk)
        else:
            form = ProfileForm(instance=profile)
        context = {
            'form' : form,
            'profile_pk' : profile_pk,
        }
        return render(request, 'accounts/update_profile.html', context)
    else:
        return redirect('accounts:profile', user_pk)


@require_POST
def delete_profile(request, user_pk, profile_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        user = request.user
        profile = Profile.objects.get(pk=profile_pk)
        if person == user:
            profile.delete()
            return redirect('accounts:profile', user_pk)
        else:
            return redirect('accounts:profile', user_pk)