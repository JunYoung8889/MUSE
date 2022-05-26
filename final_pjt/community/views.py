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
    ActorComment,
    DirectorComment,
    PeopleComment,
)
from .forms import (
    ActorForm,
    DirectorForm,
    PeopleForm,
    ActorCommentForm,
    DirectorCommentForm,
    PeopleCommentForm,
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
    article = get_object_or_404(ActorArticle, pk = actor_pk)
    person = article.user
    form = ActorCommentForm()
    context = {
        'article' : article,
        'person' : person,
        'form' : form,
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


@require_http_methods(['GET', 'POST'])
@login_required
def actor_update(request, user_pk, actor_pk):
    article = get_object_or_404(ActorArticle, pk=actor_pk)
    person = article.user
    if person == request.user:
        if request.method == 'POST':
            form = ActorForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('community:actor_detail', actor_pk)
        else:
            form = ActorForm(instance=article)
        context = {
            'form': form,
            'article': article,
            'person': person,
        }
        return render(request, 'community/actor_update.html', context)
    return redirect('community:actor_detail', actor_pk)


@require_POST
def actor_delete(request, user_pk, actor_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(ActorArticle, pk=actor_pk)
        if request.user == article.user:
            article.delete()
    return redirect('community:actor')


@require_POST
def actor_comments_create(request, actor_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(ActorArticle, pk=actor_pk)
        form = ActorCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.actor_article = article
            comment.user = request.user
            comment.save()
        return redirect('community:actor_detail', actor_pk)
    return redirect('accounts:login')


@require_POST
def actor_comments_delete(request, actor_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(ActorComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:actor_detail', actor_pk)


@login_required
@require_safe
def director(request):
    articles = DirectorArticle.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'community/director.html', context)


@login_required
@require_safe
def director_detail(request, director_pk):
    article = get_object_or_404(DirectorArticle, pk = director_pk)
    person = article.user
    form = DirectorCommentForm()
    context = {
        'article' : article,
        'person' : person,
        'form' : form,
    }
    return render(request, 'community/director_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def director_create(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect('community:director')
    else:
        form = DirectorForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/director_create.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def director_update(request, user_pk, director_pk):
    article = get_object_or_404(DirectorArticle, pk=director_pk)
    person = article.user
    if person == request.user:
        if request.method == 'POST':
            form = DirectorForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('community:director_detail', director_pk)
        else:
            form = DirectorForm(instance=article)
        context = {
            'form': form,
            'article': article,
            'person': person,
        }
        return render(request, 'community/director_update.html', context)
    return redirect('community:director_detail', director_pk)


@require_POST
def director_delete(request, user_pk, director_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(DirectorArticle, pk=director_pk)
        if request.user == article.user:
            article.delete()
    return redirect('community:director')


@require_POST
def director_comments_create(request, director_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(DirectorArticle, pk=director_pk)
        form = DirectorCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.director_article = article
            comment.user = request.user
            comment.save()
        return redirect('community:director_detail', director_pk)
    return redirect('accounts:login')


@require_POST
def director_comments_delete(request, director_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(DirectorComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:director_detail', director_pk)


@login_required
@require_safe
def people(request):
    articles = PeopleArticle.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'community/people.html', context)


@login_required
@require_safe
def people_detail(request, people_pk):
    article = get_object_or_404(PeopleArticle, pk = people_pk)
    person = article.user
    form = PeopleCommentForm()
    context = {
        'article' : article,
        'person' : person,
        'form' : form,
    }
    return render(request, 'community/people_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def people_create(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.method == 'POST':
        form = PeopleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = user
            article.save()
            return redirect('community:people')
    else:
        form = PeopleForm()
    context = {
        'form' : form,
    }
    return render(request, 'community/people_create.html', context)


@require_http_methods(['GET', 'POST'])
@login_required
def people_update(request, user_pk, people_pk):
    article = get_object_or_404(PeopleArticle, pk=people_pk)
    person = article.user
    if person == request.user:
        if request.method == 'POST':
            form = PeopleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('community:people_detail', people_pk)
        else:
            form = PeopleForm(instance=article)
        context = {
            'form': form,
            'article': article,
            'person': person,
        }
        return render(request, 'community/people_update.html', context)
    return redirect('community:people_detail', people_pk)


@require_POST
def people_delete(request, user_pk, people_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(PeopleArticle, pk=people_pk)
        if request.user == article.user:
            article.delete()
    return redirect('community:people')


@require_POST
def people_comments_create(request, people_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(PeopleArticle, pk=people_pk)
        form = PeopleCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.people_article = article
            comment.user = request.user
            comment.save()
        return redirect('community:people_detail', people_pk)
    return redirect('accounts:login')


@require_POST
def people_comments_delete(request, people_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(PeopleComment, pk=comment_pk)
        if request.user == comment.user:
            comment.delete()
    return redirect('community:people_detail', people_pk)
