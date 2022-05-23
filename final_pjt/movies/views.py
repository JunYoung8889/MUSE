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
from .forms import ReviewForm
from django.http import JsonResponse
from django.contrib.auth import get_user_model
import requests


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
    context = {
        'IMAGE_URL' : IMAGE_URL,
        'movies' : movies,
    }
    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'movie' : movie,
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
        if request.user in movie.like_users.all():
            movie.like_users.remove(request.user)
            liked = False
        else:
            movie.like_users.add(request.user)
            liked = True
        context = {
            'liked' : liked,
            'count' : movie.like_users.count(),
        }
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')