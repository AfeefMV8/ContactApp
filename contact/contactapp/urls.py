from django.urls import path

from . import views

urlpatterns = [
    path('', views.signin),
    path('signup', views.signuppage),
    path('home', views.homepage)
]
