from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('movies/', views.index, name='index'),
    path('movies/<int:movie_pk>/', views.detail, name='detail'),
    path('movies/<int:movie_pk>/reviews/', views.reviews_create, name='reviews_create'),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/delete/', views.reviews_delete, name='reviews_delete'),
    path('movies/<int:movie_pk>/like/', views.like, name='like'),
    path('movies/recommend/', views.recommend, name='recommend'),
    path('movies/search/', views.search, name='search'),
]
