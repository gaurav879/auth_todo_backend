import json

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken

from login.models import User

from .models import Task
from .serializers import EventSerializer



class Home(APIView):
    def get(self, request):
        print(request)
        var=request.headers["Authorization"].split(" ")[1]
        access_token=AccessToken(var)
        arr = Task.objects.filter(userid=access_token["user_id"])
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
        temp=request.headers["Authorization"].split(" ")[1]
        access_token=AccessToken(temp)
        var["userid"]=access_token["user_id"]
        print(var)
        serializer = EventSerializer(data=var)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


