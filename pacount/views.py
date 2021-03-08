from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from pacount.models import Field
from pacount.serializers import FieldSerializer, FieldListSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



class FieldList(APIView):
    def get(self, request, format=None):
        fields = Field.objects.all()
        serializer = FieldListSerializer(fields, many=True)
        return Response(serializer.data)