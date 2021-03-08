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


class Player(BaseModel):
    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)


class Score(BaseModel):
    par = models.IntegerField()
    score = models.IntegerField()
    hole = models.ForeignKey(to=Hole, on_delete=models.DO_NOTHING, related_name="scores")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name="scores", null=True)

    is_saved = models.BooleanField(default=False)

