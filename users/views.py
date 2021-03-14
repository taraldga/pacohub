from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny,)

        return super(UserViewSet, self).get_permissions()


class MeView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION').split(" ")[1]
        user = Token.objects.get(key=token).user
        serializer = UserSerializer(user)
        return Response(serializer.data)
