from rest_framework.views import APIView
from .models import Task
from .serializers import EventSerializer
from rest_framework.response import Response
import json


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