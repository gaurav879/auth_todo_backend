from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import json


class Signup(APIView):
    def get(self,request):
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
    def get(self,request):
        arr = User.objects.all()
        serializer = UserSerializer(arr, many=True)
        return Response(serializer.data)
    def post(self,request):
        var = json.loads(request.body)
        user = User.objects.filter(username=var["username"]).first()

        if user is None:
            # raise AuthenticationFailed("USER NOT FOUND!!!!")
            return Response("Invalid username")
        
        temp = UserSerializer(user)
        if (var["password"]==temp.data["password"]):
            return Response(temp.data["id"])
        return Response("Invalid PW")

               