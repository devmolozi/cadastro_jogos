from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Game


class Home(ListView):
    model = Game
    template_name = 'index.html'
    context_object_name = 'items'
    ordering = ('-release_year')

class NewGame(CreateView):
    model = Game
    template_name = 'new_game.html'
    fields = ['name', 'description', 'release_year', 'foto']
    
    success_url = reverse_lazy('home') 

class GameUpdateView(UpdateView):
    model = Game
    template_name = 'update.html'
    fields = ['name', 'description', 'release_year', 'foto']
    success_url = reverse_lazy('home') 

class GameDeleteView(DeleteView):
    model = Game
    template_name = 'delete_confirm.html'
    success_url = reverse_lazy('home') 


class GameDetailView(DetailView):
    model = Game
    template_name = 'detail.html'