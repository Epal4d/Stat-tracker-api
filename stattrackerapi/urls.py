from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('players/', views.get_players, name='get_players'),
    path('players/create/',views.create_player, name="create_player"),
    path('players/<int:player_id>/update/',views.update_player, name="update_player"),
    path('players/<int:player_id>/delete/',views.delete_player, name="delete_player"),
    path('matches/', views.get_matches, name='get_matches')
]