from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
