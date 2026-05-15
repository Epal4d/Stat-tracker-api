"""Views for match endpoints."""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from stattrackerapi.models import Match


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_matches(request):
    """Returns all matches belonging to the authenticated coach."""
    matches = Match.objects.filter(coach=request.user)
    match_list = []
    for match in matches:
        match_list.append({
            'id': match.id,
            'opponent_name': match.opponent_name,
            'date': match.date,
            'location': match.location,
            'match_type': match.match_type.name if match.match_type else None,
            'team_score': match.team_score,
            'opponent_score': match.opponent_score,
        })
    return Response(match_list, status=status.HTTP_200_OK)