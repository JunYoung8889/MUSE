from django.urls import path
from. import views


app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.profile, name='profile'),
    path('<int:user_pk>/create/', views.create_profile, name="create_profile"),
    path('<int:user_pk>/<int:profile_pk>/update/', views.update_profile, name="update_profile"),
    path('<int:user_pk>/<int:profile_pk>/delete/', views.delete_profile, name="delete_profile"),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]
