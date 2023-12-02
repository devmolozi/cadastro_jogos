from django.contrib import admin
from games.models import Game

# Register your models here.
class GameAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Game, GameAdmin)