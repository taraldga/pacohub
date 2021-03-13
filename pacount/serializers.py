from django.contrib.auth.models import User
from rest_framework import serializers
from pacount.models import Field, Hole, CreateGameRequest, Game, Player, Score


class HoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hole
        fields = ['number', 'par']


class FieldListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['name', 'city']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

class PlayerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Player
        fields = ['user']


class ScoreSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)

    class Meta:
        model = Score
        fields = ['par', 'score', 'player', 'player_name']


class FieldSerializer(serializers.ModelSerializer):
    holes = HoleSerializer(many=True, read_only=True)

    class Meta:
        model = Field
        fields = ['name', 'holes']


class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    field = FieldSerializer(read_only=True)
    scores = ScoreSerializer(many=True, read_only=True)

    field_id = serializers.IntegerField(write_only=True)
    player_ids = serializers.ListField(child=serializers.IntegerField(), required=False)
    player_names = serializers.ListField(child=serializers.CharField(), allow_null=True)

    is_finished = serializers.BooleanField(allow_null=True, read_only=True)

    def create(self, validated_data):
        player_ids = validated_data.pop('player_ids', [])
        player_names = validated_data.pop('player_names', [])
        field_id = validated_data.get('field_id')
        field = Field.objects.get(pk=field_id)

        game = Game.objects.create(field=field)
        scores = []
        for hole in field.holes.all():
            for player_name in player_names:
                scores.append(Score.objects.create(
                    game=game,
                    player_name=player_name,
                    hole=hole,
                    par=hole.par,
                    score=0
                ))
            for player_id in player_ids:
                try:
                    player = Player.objects.get(pk=player_id)
                    scores.append(Score.objects.create(
                        game=game,
                        player=player,
                        hole=hole,
                        par=hole.par,
                        score=0
                    ))
                except Player.DoesNotExist:
                    pass
        return game
