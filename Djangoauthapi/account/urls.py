
from django.urls import path
from account.views import UserRegistraionsViews, UserLoginView,UserProfileView,UserChangePasswordView

urlpatterns = [
   
    path('register/', UserRegistraionsViews.as_view(), name="register"),
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="UserProfileView"),
    path('changepassword/', UserChangePasswordView.as_view(), name="changepassword"),
]