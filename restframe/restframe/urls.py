

from django.contrib import admin
from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route1 = DefaultRouter()
route.register('studentapi', views.StudentViewset, basename='studentapi')
route1.register('studentapi1', views.StudentModelViewset, basename='studentapi1')

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

    
    # Generic Api

    path("stulist/", views.StudentList.as_view()),
    path("stucreate/", views.StudentCreate.as_view()),
    path("stureterive/<int:pk>/", views.StudentRetrive.as_view()),
    path("stuupdate/<int:pk>/", views.StudentUpdate.as_view()),

    path("slc/", views.StudentListCreate.as_view()),
    path("slc/<int:pk>/", views.StudentRetriveUpdate.as_view()),
    path("slcd/<int:pk>/", views.StudentRetriveDestroy.as_view()),
    path("slrcd/<int:pk>/", views.StudentRetriveUpdateDestroy.as_view()),


    # ViewSet
    path("", include(route.urls)),
    path("api/", include(route1.urls)),


]

