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
            'position_id': player.position_id,
            'birthday': player.birthday,
        })
    return Response(player_list, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_player(request):
    """Creates a new player and assigns them to the authenticated coach """
    position_id = request.data.get('position_id')
    name = request.data.get('name')
    jersey_number = int(request.data.get('jersey_number'))
    birthday = request.data.get('birthday')

    if not name or not jersey_number:
        return Response(
            {'error': 'Name and jersey number required'},
            status=status.HTTP_400_BAD_REQUEST
        )
    player =Player.objects.create(
        coach=request.user,
        name=name,
        jersey_number=jersey_number,
        birthday=birthday,
        position_id=position_id
    )

    return Response(
        {
            'id': player.id,
            'name': player.name,
            'jersey_number': player.jersey_number,
            'position': player.position.name if player.position else None,
            'position_id': player.position_id,
            'birthday': player.birthday
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_player(request, player_id):
    """Updates an existing player that belongs to an authenticated coach"""
    player = get_object_or_404(Player, id=player_id, coach=request.user)

    player.name = request.data.get('name', player.name)
    player.jersey_number = request.data.get('jersey_number', player.jersey_number)
    player.birthday = request.data.get('birthday', player.birthday)
    player.position_id = request.data.get('position_id', player.position_id)
    player.save()

    return Response(
        {
            'id': player.id,
            'name': player.name,
            'jersey_number': player.jersey_number,
            'position' : player.position.name if player.position else None,
            'position_id' : player.position_id,
            'birthday': player.birthday
        },
        status=status.HTTP_200_OK
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_player(request, player_id):
    """ DELETES a player from a coaches team"""
    player = get_object_or_404(Player, id = player_id, coach= request.user)
    player.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)
