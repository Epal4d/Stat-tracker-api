from django import models


class MatchType(models.Model):
    """Represents the type of match played"""
    name = models.CharField(max_length=50)

    def __str___(self):
        return self.name
