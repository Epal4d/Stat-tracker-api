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
