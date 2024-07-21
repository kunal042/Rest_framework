from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer



@api_view(['GET', 'POST', "PUT","PATCH", "DELETE"])
def Student_api(request, pk = None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "msg" : "Data Created"
            })
        return Response(serializer.errors)
        
    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : "Data fully update Upated"})
        return Response(serializer.errors)
    
    if request.method == "PUT":
        id = pk
        stu = Student.objects.get(pk = id)
        serializer = StudentSerializer(stu, partial=True, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : "Data Paticial  Upated"})
        return Response(serializer.errors)
        
    if request.method == "DELETE":
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({
            'msg' : "Data Deleted Sucessfully!!!"       })


        
        
