from django.urls import path
from calorieapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert_meal, name='insert_meal'),
    path('edit/<int:id>/', views.edit_meal, name='edit_meal'),
    path('update/<int:id>/', views.update_meal, name='update_meal'),
    path('delete/<int:id>/', views.delete_meal, name='delete_meal'),
]