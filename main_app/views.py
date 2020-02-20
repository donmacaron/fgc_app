from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Game
from .forms import GameForm


# Create your views here.
def show(request):
    game_list = Game.objects.filter().order_by('-score')
    form = GameForm()

    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        data = request.POST.copy()
        if form.is_valid():
            post = form.save(commit = False)
            post.check_existing_game(data.get('game_title'))
            return redirect('home')
        else:
            return redirect('home')
    elif request.method == 'GET':
        form = GameForm()
        return render(request, 'main_app/index.html', {'game_list': game_list,
                                                       'form': form})


# class HomePageView(ListView):
#     model = Game
#     form_class = GameForm
#     template_name = 'home.html'
#     success_url = reverse_lazy('home')
#
#
# class CreateGameView(CreateView):
#     model = Game
#     form_class = GameForm
#     template_name = 'main_app/add_game.html'
#     success_url = reverse_lazy('home')
