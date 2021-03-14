from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel

# Create your models here.


class Field(BaseModel):
    name = models.TextField()
    city = models.TextField()

    def __str__(self):
        return self.name


class Hole(BaseModel):
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="holes")
    number = models.IntegerField()
    par = models.IntegerField()


class Game(BaseModel):
    isFinished = models.BooleanField(default=False)
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, related_name="games")
    playerNames = models.TextField(null=True)


class Player(BaseModel):
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    name = models.TextField(null=True)


class Score(BaseModel):
    par = models.IntegerField()
    score = models.IntegerField()
    hole = models.ForeignKey(to=Hole, on_delete=models.DO_NOTHING, related_name="scores")
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="scores", null=True)
    player_name = models.TextField(null=True)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE, related_name="scores")

    is_saved = models.BooleanField(default=False)


class CreateGameRequest:
    field_id = 0
    player_ids = []
    player_names = []