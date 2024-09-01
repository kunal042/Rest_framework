

from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Fuction Based 
    path('student/', views.student_list, name='student'),
    path('student/<int:pk>/', views.student_list, name='student'),

    # Class Based : 

    path('studentapi/',views.StudenApi.as_view(), name="stu"),
    path('studentapi/<int:pk>/',views.StudenApi.as_view(), name="stu1"),

    # Generic view

    path('stuapi/', views.StudentList.as_view()),
    path('stuapicreate/', views.StudentCreate.as_view()),
    path('stuapiretrive/<int:pk>/', views.StudentRetrive.as_view()),
    path('stuapiupdate/<int:pk>/', views.StudentUpdate.as_view()),
    path('stuapidelete/<int:pk>/', views.StudentDelete.as_view()),



    path('stulc/', views.LCStudent.as_view()),
    path('stulc/<int:pk>/', views.RUDStudent.as_view()),

    

]

