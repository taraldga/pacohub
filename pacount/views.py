from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pacount.models import Field, Game, Score
from pacount.serializers import ScoreSerializer, FieldListSerializer, GameSerializer, GameListSerializer, ShallowScoreSerializer
from rest_framework import status, generics, viewsets


class FieldList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        fields = Field.objects.all()
        serializer = FieldListSerializer(fields, many=True)
        return Response(serializer.data)


class ScoreView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class BulkUpdateScoreView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Score.objects.all()

    def patch(self, request, *args, **kwargs):
        data = request.data
        for row in data:
            try:
                element = Score.objects.get(pk=row["id"])
                serializer = ShallowScoreSerializer(data=row, partial=True, instance=element)
                if serializer.is_valid():
                    serializer.save()
                else:
                    continue
            except Score.DoesNotExist:
                continue
        return Response(status=status.HTTP_200_OK)


class GameView(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        try:
            return Game.objects.get(pk=pk)
        except Game.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk,  format=None):
        game = self.get_object(pk)
        serializer = GameSerializer(data=request.data, instance=game, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        game = self.get_object(pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        games = Game.objects.all()
        serializer = GameListSerializer(games, many=True)
        return Response(serializer.data)