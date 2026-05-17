"""Views for player match stat endpoints."""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from stattrackerapi.models import PlayerMatch, Match


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_player_stats(request, match_id):
    """Returns all player stats for a specific match."""
    match = get_object_or_404(Match, id=match_id, coach=request.user)
    stats = PlayerMatch.objects.filter(match=match)
    stats_list = []
    for stat in stats:
        stats_list.append({
            'id': stat.id,
            'player_id': stat.player.id,
            'player_name': stat.player.name,
            'goals': stat.goals,
            'assists': stat.assists,
            'minutes': stat.minutes,
            'yellow_cards': stat.yellow_cards,
            'red_cards': stat.red_cards,
            'shots_taken': stat.shots_taken,
        })
    return Response(stats_list, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_player_stat(request, match_id):
    """Records stats for a player in a specific match."""
    match = get_object_or_404(Match, id=match_id, coach=request.user)
    player_id = request.data.get('player_id')
    
    if not player_id:
        return Response(
            {'error': 'Player id is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    stat = PlayerMatch.objects.create(
        match=match,
        player_id=player_id,
        goals=request.data.get('goals', 0),
        assists=request.data.get('assists', 0),
        minutes=request.data.get('minutes', 0),
        yellow_cards=request.data.get('yellow_cards', 0),
        red_cards=request.data.get('red_cards', 0),
        shots_taken=request.data.get('shots_taken', 0),
    )

    return Response(
        {
            'id': stat.id,
            'player_id': stat.player.id,
            'player_name': stat.player.name,
            'goals': stat.goals,
            'assists': stat.assists,
            'minutes': stat.minutes,
            'yellow_cards': stat.yellow_cards,
            'red_cards': stat.red_cards,
            'shots_taken': stat.shots_taken,
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_player_stat(request, match_id, stat_id):
    """Updates an existing player stat entry for a specific match."""
    match = get_object_or_404(Match, id=match_id, coach=request.user)
    stat = get_object_or_404(PlayerMatch, id=stat_id, match=match)

    stat.goals = request.data.get('goals', stat.goals)
    stat.assists = request.data.get('assists', stat.assists)
    stat.minutes = request.data.get('minutes', stat.minutes)
    stat.yellow_cards = request.data.get('yellow_cards', stat.yellow_cards)
    stat.red_cards = request.data.get('red_cards', stat.red_cards)
    stat.shots_taken = request.data.get('shots_taken', stat.shots_taken)
    stat.save()

    return Response(
        {
            'id': stat.id,
            'player_id': stat.player.id,
            'player_name': stat.player.name,
            'goals': stat.goals,
            'assists': stat.assists,
            'minutes': stat.minutes,
            'yellow_cards': stat.yellow_cards,
            'red_cards': stat.red_cards,
            'shots_taken': stat.shots_taken,
        },
        status=status.HTTP_200_OK
    )