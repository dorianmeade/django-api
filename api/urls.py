from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"), 
    path('esco/<str:title>', views.career, name="career"), 

]