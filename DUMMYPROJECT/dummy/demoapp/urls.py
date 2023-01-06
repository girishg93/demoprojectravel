from . import views
from django.urls import path

urlpatterns = [


    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus1'),


]
"""path('',views.home,name='home'),
  path('operations/',views.addition,name='addition'),"""
