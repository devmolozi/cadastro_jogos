from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    release_year = models.IntegerField('Lançamento')
    description = models.TextField('Descrição')
    foto = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name


    
