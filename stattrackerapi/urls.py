from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('players/', views.get_players, name='get_players'),
    path('players/create/',views.create_players, name="create_players"),
    path('players/<int:player_id>/',views.update_players, name="update_players")
]