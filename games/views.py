from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game


class Home(ListView):
    model = Game
    template_name = 'index.html'
    context_object_name = 'items'
    ordering = ('-id')

class NewGame(CreateView):
    model = Game
    template_name = 'new_game.html'
    fields = ['name', 'release_year']
    success_url = reverse_lazy('home') 

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'update.html'
    fields = ['name', 'release_year']
    success_url = reverse_lazy('home') 

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home') 