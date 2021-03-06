import json
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer


class Signup(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        arr = User.objects.all()
        serializer = UserSerializer(arr, many=True)
        return Response(serializer.data)

    def post(self, request):
        var = json.loads(request.body)
        serializer = UserSerializer(data=var)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    permission_classes=[AllowAny]
    def get(self, request):
        arr = User.objects.all()
        serializer = UserSerializer(arr, many=True)
        return Response(serializer.data)

    def post(self, request):
        var = json.loads(request.body)
        user = User.objects.filter(username=var["username"]).first()

        if user is None:
            return Response("Invalid username", status=404)

        temp = UserSerializer(user)
        if var["password"] == temp.data["password"]:
            refresh = RefreshToken.for_user(user)

            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
        return Response("Invalid PW", status=404)
