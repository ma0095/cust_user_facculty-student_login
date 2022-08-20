from django.contrib import admin
from django.urls import path
from myusers import views

urlpatterns = [
    path("register",views.EmpCreateView.as_view(),name="signup"),
    path("login",views.LoginView.as_view(),name="signin")

]
