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
    path('director/', views.director, name="director"),
    path('people/', views.people, name="people"),
]
