from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.home, name="home"),
    path('actor/', views.actor, name="actor"),
    path('actor/<int:actor_pk>/', views.actor_detail, name="actor_detail"),
    path('actor/<int:user_pk>/create/', views.actor_create, name="actor_create"),
    path('actor/<int:user_pk>/<int:actor_pk>/update/', views.actor_update, name="actor_update"),
    path('actor/<int:user_pk>/<int:actor_pk>/delete/', views.actor_delete, name="actor_delete"),
    path('actor/<int:actor_pk>/comments/', views.actor_comments_create, name='actor_comments_create'),
    path('actor/<int:actor_pk>/comments/<int:comment_pk>/delete/', views.actor_comments_delete, name='actor_comments_delete'),
    path('director/', views.director, name="director"),
    path('director/<int:director_pk>/', views.director_detail, name="director_detail"),
    path('director/<int:user_pk>/create/', views.director_create, name="director_create"),
    path('director/<int:user_pk>/<int:director_pk>/update/', views.director_update, name="director_update"),
    path('director/<int:user_pk>/<int:director_pk>/delete/', views.director_delete, name="director_delete"),
    path('director/<int:director_pk>/comments/', views.director_comments_create, name='director_comments_create'),
    path('director/<int:director_pk>/comments/<int:comment_pk>/delete/', views.director_comments_delete, name='director_comments_delete'),
    path('people/', views.people, name="people"),
    path('people/<int:people_pk>/', views.people_detail, name="people_detail"),
    path('people/<int:user_pk>/create/', views.people_create, name="people_create"),
    path('people/<int:user_pk>/<int:people_pk>/update/', views.people_update, name="people_update"),
    path('people/<int:user_pk>/<int:people_pk>/delete/', views.people_delete, name="people_delete"),
    path('people/<int:people_pk>/comments/', views.people_comments_create, name='people_comments_create'),
    path('people/<int:people_pk>/comments/<int:comment_pk>/delete/', views.people_comments_delete, name='people_comments_delete'),
]
