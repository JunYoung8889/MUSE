from django.shortcuts import (
    render,
    redirect,
    get_list_or_404,
    get_object_or_404,
)
from .models import (
    ActorArticle,
    DirectorArticle,
    PeopleArticle,
)
from .forms import (
    ActorForm,
    DirectorForm,
    PeopleForm,
)
from django.contrib.auth import get_user_model
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
@require_safe
def home(request):
    return render(request, 'community/home.html')


@login_required
@require_safe
def actor(request):
    articles = ActorArticle.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'community/actor.html', context)


@login_required
@require_safe
def actor_detail(request, actor_pk):
    article = ActorArticle.objects.get(pk = actor_pk)
    context = {
        'article' : article,
    }
    return render(request, 'community/actor_detail.html', context)
    

@login_required
@require_http_methods(['GET', 'POST'])
def actor_create(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect('community:actor')
    else:
        form = ActorForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/actor_create.html', context)


def actor_update(request, user_pk, actor_pk):
    pass


def actor_delete(request, user_pk, actor_pk):
    pass


@login_required
def director(request):
    return render(request, 'community/director.html')


@login_required
def people(request):
    return render(request, 'community/people.html')