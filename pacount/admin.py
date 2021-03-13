from django.contrib import admin
from pacount.models import Field, Hole, Score, Game

# Register your models here.


class HoleAdmin(admin.options.TabularInline):
    model = Hole


class FieldAdmin(admin.ModelAdmin):
    inlines = [HoleAdmin, ]


class ScoreAdmin(admin.ModelAdmin):
    model = Score


class GameAdmin(admin.ModelAdmin):
    model = Game


admin.site.register(Field, FieldAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Game, GameAdmin)