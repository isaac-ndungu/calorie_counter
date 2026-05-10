from django.shortcuts import render
from .models import Meal

def index(request):
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'index.html', context)
