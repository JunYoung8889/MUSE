from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('<int:movie_pk>/reviews/', views.reviews_create, name='reviews_create'),
    path('<int:movie_pk>/reviews/<int:review_pk>/delete/', views.reviews_delete, name='reviews_delete'),
    path('<int:movie_pk>/like/', views.like, name='like'),
]
