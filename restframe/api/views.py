from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializers



# function based on api
from rest_framework.decorators import  api_view

# Common
from rest_framework.response import Response
from rest_framework import status


# Class Based 
from rest_framework.decorators import APIView

# Generic Api View
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


@api_view(['GET', 'POST', 'PUT', 'PATCH', "DELETE"])
def student_list(request, pk = None):
    pk = pk 

    if request.method == "GET":
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    

    if request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data , status=status.HTTP_201_CREATED)  #{'Msg' : 'Data Created'},
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data is Complete Update!!'})
        return Response(serializer.errors)
    
    if request.method == "PATCH":
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializers(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'Msg' : 'Partical Data Updated!!'})
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'Msg' : "Data Delete"})
    

# Class Based View :
    
class StudenApi(APIView):
    def get(self,request, pk=None, format=None):
        pk = pk
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializers(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
        

    
    def post(self, request, pk=None, formate=None):
        pk = pk 
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Data is Created!!!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        pk = pk
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Msg" : "Complete Data is Update!!1"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request, pk, formate=None):
        pk = pk 
        stu = Student.objects.get(pk=pk)
        serailizer = StudentSerializers(stu, data=request.data, partial=True)
        if serailizer.is_valid():
            serailizer.save()
            return Response({'Msg' : "Data is Paricial Created!!!"}, status=status.HTTP_201_CREATED)
        return Response(serailizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk,  formate=None):
        pk = pk 
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({'Msg' : "Data is Delted!!!"})


# Generic  Api Views 

class StudentList(GenericAPIView, ListModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request,  *args, **kwargs):
        return self.list(request,*args, **kwargs)
    

class StudentCreate(GenericAPIView, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    
class StudentRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)   
    
class StudentUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
class StudentDelete(GenericAPIView, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class LCStudent(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class RUDStudent(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)    

    

