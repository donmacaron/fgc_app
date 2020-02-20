from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.
class Game(models.Model):
    game_title = models.CharField(max_length = 64)
    game_description = models.CharField(max_length = 240, null = True)
    cover = models.ImageField(upload_to = 'images/covers', default = 'images/none/default.png')
    score = models.IntegerField(null = True)
    date = models.DateTimeField(blank = True, null = True)
    was_streamed = models.BooleanField(null = True)
    when_streamed = models.DateTimeField(blank = True, null = True)
    stream_list = models.CharField(max_length = 1024, null = True)

    def __str__(self):
        return self.game_title


    def publish(self):
        self.was_streamed = False
        self.score = 1
        self.date = timezone.now()
        self.save()


    def check_existing_game(self, game_name):
        game_list = Game.objects.all()
        for game in game_list:
            if self.game_title.lower().replace(' ', '') == game.game_title.lower().replace(' ', ''):
                game.score += 1
                game.save()
                break
        else:
            self.publish()
