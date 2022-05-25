from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'community/home.html')
    else:
        return redirect('accounts:login')


def actor(request):
    if request.user.is_authenticated:
        return render(request, 'community/actor.html')
    else:
        return redirect('accounts:login')