from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Field(models.Model):
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)


class Hole(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name="holes")
    number = models.IntegerField()
    par = models.IntegerField()


class Game(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    isFinished = models.BooleanField(default=False)
    field = models.ForeignKey(Field, on_delete=models.DO_NOTHING, related_name="games")


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    user = models.OneToOneField(to=User, null=True, on_delete=models.CASCADE)
    name = models.TextField(null=True)
    game = models.ForeignKey(to=Game, on_delete=models.CASCADE)


class Score(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    par = models.IntegerField()
    score = models.IntegerField()
    hole = models.ForeignKey(to=Hole, on_delete=models.DO_NOTHING, related_name="scores")
    player = models.ForeignKey(to=Player, on_delete=models.CASCADE, related_name="scores", null=True)

    is_saved = models.BooleanField(default=False)

