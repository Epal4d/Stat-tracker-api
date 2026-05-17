from django.db import models
from .player import Player
from .match import Match


class PlayerMatch(models.Model):
    """Represents a player's stats for a specific match"""
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='match_stats')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_stats')
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    shots_taken = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.player.name} - {self.match.opponent_name}"
