from django.shortcuts import render
from django.contrib.auth import authenticate

from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


from .models import User
from .seializers import UserRegistraionsSerializers, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer
from account.renderers import UserRenderes


# Generate Token Manually
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class UserRegistraionsViews(APIView) :
    renderer_classes = [UserRenderes]
    def post(self, request, formate=None):
        serializer = UserRegistraionsSerializers( data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response({'token' :token ,'Msg' : 'Registraion Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    renderer_classes = [UserRenderes]
    def post(self, request, formate=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            token = get_tokens_for_user(user)
            if user is not None:
                return Response({'token':token ,'Msg' : "Login Sucess"}, status=status.HTTP_200_OK)
            else:
                return Response({'errors' : {'non_field_errors' : ['Email or Password is not valid!!']}}, status=status.HTTP_404_NOT_FOUND)
            

class UserProfileView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]
    def get(self, request, formate=None ):
        serializer = UserProfileSerializer(request.user)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderes]
    permission_classes = [IsAuthenticated]
    def Post(self, request, formate=None):
        serializer = UserChangePasswordSerializer(data = request.data, context={'user' :request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"Msg" : "Password Change Sucessfully!!"}, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)