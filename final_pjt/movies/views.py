from django.shortcuts import (
    render,
    get_list_or_404,
    get_object_or_404,
    redirect,
)
from django.views.decorators.http import (
    require_http_methods,
    require_POST,
    require_safe,
)
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Genre
from .forms import ReviewForm, ReviewUpdateForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import requests
from django.core.paginator import Paginator
import math
import random


# Create your views here.
@require_safe
def main(request):
    return render(request, 'movies/main.html')


@require_safe
def index(request):
    movies = Movie.objects.all()
    IMAGE_URL = 'https://image.tmdb.org/t/p/original'
    if len(movies) == 0:
        genres = requests.get('https://api.themoviedb.org/3/genre/movie/list?api_key=82fd037e84e453b9ff4e74d5eb529e7f&language=ko-KR').json().get('genres')
        for genre in genres:
            genre_save = Genre()
            genre_save.id = genre['id']
            genre_save.name = genre['name']
            genre_save.save()
        genres = Genre.objects.all()
        API_KEY = '82fd037e84e453b9ff4e74d5eb529e7f'
        BASE_URL = 'https://api.themoviedb.org/3/movie/popular'
        for i in range(1,4):
            params = {
                'api_key' : API_KEY,
                'page' : i,
                'language' : 'ko-KR',
            }
            response = requests.get(BASE_URL, params = params).json()
            movie_list = response.get('results')
            for movie in movie_list:
                movie_save = Movie()
                movie_save.id = movie['id']
                movie_save.title = movie['title']
                if movie['release_date'] == "":
                    movie_save.release_date = '1000-01-01'
                else:
                    movie_save.release_date = movie['release_date']
                movie_save.popularity = movie['popularity']
                movie_save.vote_count = movie['vote_count']
                movie_save.vote_average = movie['vote_average']
                movie_save.overview = movie['overview']
                movie_save.poster_path = movie['poster_path']
                movie_save.save()
                for genre_id in movie['genre_ids']:
                    movie_save.genres.add(genre_id)
        movies = Movie.objects.all()
    paginator = Paginator(movies, 12)
    page = request.GET.get('page')
    last_page = str(math.ceil(movies.count()/12))
    posts = paginator.get_page(page)
    context = {
        'IMAGE_URL' : IMAGE_URL,
        'movies' : movies,
        'posts' : posts,
        'page' : page,
        'last_page' : last_page,
    }
    return render(request, 'movies/index.html', context, )


@require_safe
def detail(request, movie_pk):
    IMAGE_URL = 'https://image.tmdb.org/t/p/original'
    movie = get_object_or_404(Movie, pk=movie_pk)
    form = ReviewForm()
    context = {
        'movie' : movie,
        'IMAGE_URL' : IMAGE_URL,
        'form' : form,
    }
    return render(request, 'movies/detail.html', context)


@require_POST
def reviews_create(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
        return redirect('movies:detail', movie.pk)
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
@login_required
def reviews_update(request, movie_pk, review_pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    if user == review.user:
        if request.method == 'POST':
            form = ReviewUpdateForm(request.POST, instance=review)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie_pk)
        else:
            form = ReviewUpdateForm(instance=review)
        context = {
            'form': form,
            'movie': movie,
            'review': review,
        }
        return render(request, 'movies/reviews_update.html', context)
    else:
        return redirect('movies:detail', movie_pk)


@require_POST
def reviews_delete(request, movie_pk, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review, pk=review_pk)
        if request.user == review.user:
            review.delete()
    return redirect('movies:detail', movie_pk)


@require_POST
def like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        
        if user in movie.like_users.all():
            movie.like_users.remove(user)
            like = False
        else:
            movie.like_users.add(user)
            like = True
        context = {
            'like' : like,
            'count' : movie.like_users.count(),
        }
        return JsonResponse(context)
    return redirect('accounts:login')


def recommend(request):
    IMAGE_URL = 'https://image.tmdb.org/t/p/original'
    if request.user.is_authenticated:
        user = request.user
        genre_dict = dict()
        movies = user.like_movies.all()
        if len(movies) == 0:
            title = '랜덤'
            movies = get_list_or_404(Movie)
            picked_movies = random.sample(movies, 8)
        else:
            for movie in movies:
                genres = movie.genres.all()
                for genre in genres:
                    if genre_dict.get(genre.pk) == None:
                        genre_dict[genre.pk] = 1
                    else:
                        genre_dict[genre.pk] += 1
            max_genre_ids = []
            max_genre_nums = 0
            for genre_id in genre_dict:
                if genre_dict[genre_id] > max_genre_nums:
                    max_genre_ids = [genre_id]
                    max_genre_nums = genre_dict[genre_id]
                elif genre_dict[genre_id] == max_genre_nums:
                    max_genre_ids.append(genre_id)
            max_genre_id = random.choice(max_genre_ids)
            genre = Genre.objects.get(pk=max_genre_id)
            title = genre.name
            movies = genre.movie_set.all()
            if len(movies) <= 8:
                picked_movies = movies
            else:
                picked_movies = random.sample(list(movies), 8)
    else:
        title = '랜덤'
        movies = get_list_or_404(Movie)
        picked_movies = random.sample(movies, 8)
    context = {
        'picked_movies' : picked_movies,
        'IMAGE_URL' : IMAGE_URL,
        'title' : title,
    }
    return render(request, 'movies/recommend.html', context)


@require_POST
def search(request):
    IMAGE_URL = 'https://image.tmdb.org/t/p/original'
    title = request.POST.get('q')
    title = title.strip()
    if title == '':
        search_movies = []
        context = {
            'search_movies' : search_movies,
            'IMAGE_URL' : IMAGE_URL,
            'title' : title,
        }
        return render(request, 'movies/search.html', context)
    movies = get_list_or_404(Movie)
    search_movies = []
    for movie in movies:
        if title in movie.title:
            search_movies.append(movie)
    if search_movies == []:
        for movie in movies:
            str1 = title
            M = len(str1)
            str2 = movie.title
            N = len(str2)
            LCS = [[0]*(M+1)]+[[0]*(M+1) for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    if str2[i] == str1[j]:
                        LCS[i+1][j+1] = LCS[i][j] + 1
                    else:
                        LCS[i+1][j+1] = max(LCS[i][j+1], LCS[i+1][j])
            if max(map(max, LCS)) > M/2:
                search_movies.append(movie)
    context = {
        'search_movies' : search_movies,
        'IMAGE_URL' : IMAGE_URL,
        'title' : title,
    }
    return render(request, 'movies/search.html', context)