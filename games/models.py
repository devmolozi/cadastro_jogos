from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=255, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")
    release_year = models.IntegerField(verbose_name="Ano")
    foto = models.ImageField(upload_to='game_photos/', null=True, blank=True, verbose_name="")

    def __str__(self) -> str:
        return self.name


    
