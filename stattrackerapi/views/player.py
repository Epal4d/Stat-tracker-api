"""Views for player endpoints."""
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from stattrackerapi.models import Player


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_players(request):
    """Returns all players belonging to the authenticated coach."""
    players = Player.objects.filter(coach=request.user)
    player_list = []
    for player in players:
        player_list.append({
            'id': player.id,
            'name': player.name,
            'jersey_number': player.jersey_number,
            'position': player.position.name if player.position else None,
            'birthday': player.birthday,
        })
    return Response(player_list, status=status.HTTP_200_OK)