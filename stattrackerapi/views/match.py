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
            'match_type_id': match.match_type_id,
            'team_score': match.team_score,
            'opponent_score': match.opponent_score,
        })
    return Response(match_list, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_match(request):
    """Creates a new match and assigns it to the authenticated coach."""
    opponent_name = request.data.get('opponent_name')
    date = request.data.get('date')
    location = request.data.get('location')
    match_type_id = request.data.get('match_type_id')
    team_score = request.data.get('team_score', 0)
    opponent_score = request.data.get('opponent_score', 0)

    if not opponent_name or not date:
        return Response(
            {'error': 'Opponent name and date are required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    match = Match.objects.create(
        coach=request.user,
        opponent_name=opponent_name,
        date=date,
        location=location,
        match_type_id=match_type_id,
        team_score=team_score,
        opponent_score=opponent_score
    )

    return Response(
        {
            'id': match.id,
            'opponent_name': match.opponent_name,
            'date': match.date,
            'location': match.location,
            'match_type': match.match_type.name if match.match_type else None,
            'team_score': match.team_score,
            'opponent_score': match.opponent_score,
        },
        status=status.HTTP_201_CREATED
    )

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_match(request, match_id):

    """Updates an existing match that belongs to the authenticated coach."""
    match = get_object_or_404(Match, id=match_id, coach=request.user)

    match.opponent_name = request.data.get('opponent_name', match.opponent_name)
    match.date = request.data.get('date', match.date)
    match.location = request.data.get('location', match.location)
    match.match_type_id = request.data.get('match_type_id', match.match_type_id)
    match.team_score = request.data.get('team_score', match.team_score)
    match.opponent_score = request.data.get('opponent_score', match.opponent_score)
    match.save()

    return Response(
        {
            'id': match.id,
            'opponent_name': match.opponent_name,
            'date': match.date,
            'location': match.location,
            'match_type': match.match_type.name if match.match_type else None,
            'team_score': match.team_score,
            'opponent_score': match.opponent_score,
        },
        status=status.HTTP_200_OK
    )

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_match(request, match_id):
    """Deletes a match that belongs to the authenticated coach."""
    match = get_object_or_404(Match, id=match_id, coach=request.user)
    match.delete()
    return Response(None, status=status.HTTP_204_NO_CONTENT)