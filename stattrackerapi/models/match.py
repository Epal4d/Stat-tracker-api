from django.db import models
from django.contrib.auth.models import User
from .match_type import MatchType


class Match(models.Model):
    """Represents a match played by the coaches team."""
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='matches')
    match_type = models.ForeignKey(MatchType, on_delete=models.SET_NULL, null= True)
    date = models.DateField()
    location = models.CharField(max_length= 50)
    opponent_name = models.CharField(max_length=25)
    team_score = models.IntegerField(default=0)
    opponent_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.opponent_name} - {self.date}"
