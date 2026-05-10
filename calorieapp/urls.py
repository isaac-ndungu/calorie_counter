from django.urls import path
from calorieapp import views

urlpatterns = [
    path('', views.index, name='index')
]