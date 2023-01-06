from . import views
from django.urls import path

urlpatterns = [


    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('logout1',views.logout,name='logout1'),



]