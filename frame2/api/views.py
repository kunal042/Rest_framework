from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializer import StudentSerializer

from rest_framework import status

# Create your views here.


class StudentAPI(APIView):

    def get(self, request, formate=None, pk = None ):
        id =pk 
        if id is not None:
            stu = Student.objects.get(pk= id)
            serilazier = StudentSerializer(stu)
            return Response(serilazier.data)
        
        stu = Student.objects.all()
        serilazier = StudentSerializer(stu, many=True)
        return Response(serilazier.data)
    
    def post(self, request, formate=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'msg' : 'Data Created'},
                status=status.HTTP_201_CREATED
            )
        return(Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        ))
    
    def put(self, request, pk,formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg' : 'Complete Data Update'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def patch(self, request, pk,formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'msg' : 'Partial Data Update'
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk,formate=None):
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()

        return Response({
            'msg' : 'Data Deleted!!!'
        })