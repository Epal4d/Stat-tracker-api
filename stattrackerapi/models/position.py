from django.db import models

class Position(models.Model):
    """Represents a player position"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name