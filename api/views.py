import json

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken

from login.models import User

from .models import Task
from .serializers import EventSerializer

JWT_authenticator = JWTAuthentication()


class Home(APIView):
    def get(self, request):
        arr = Task.objects.all()
        serializer = EventSerializer(arr, many=True)
        return Response(serializer.data)

    def delete(self, request):
        var = json.loads(request.body)
        Task.objects.get(id=var["id"]).delete()
        return Response("Task Deleted")

    def put(self, request):
        var = json.loads(request.body)
        print(var)
        item = Task.objects.filter(id=var["id"]).first()
        item.status = var["status"]
        item.task = var["task"]
        item.save()
        print(item)
        return Response("updated")

    def post(self, request):
        var = json.loads(request.body)
        serializer = EventSerializer(data=var)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Data(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        var = json.loads(request.body)
        print(var)
        token_str = var["jwt"]
        access_token = AccessToken(token_str)
        user = Task.objects.filter(userid=access_token["user_id"])
        print(user)
        serializer = EventSerializer(user, many=True)
        return Response(serializer.data)
