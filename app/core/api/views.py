from core.api.serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer


class TokenCheckAPIView(APIView):
    def get(self, request, *args, **kwargs):
        auth_token = request.META.get("HTTP_AUTHORIZATION")

        if auth_token:
            print(auth_token.split()[1])
            token = Token.objects.filter(key=auth_token.split()[1])
            if token.exists():
                serializer = UserSerializer(token.first().user)
                return Response(serializer.data)
            return Response({"detail": "Invalid Token"}, status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Provide a token"}, status.HTTP_400_BAD_REQUEST)
