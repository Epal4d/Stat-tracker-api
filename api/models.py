from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    """Represents a player position"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Player(models.Model):
    """Represents a soccer player on a coach's roster with their profile information"""
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='players')
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name