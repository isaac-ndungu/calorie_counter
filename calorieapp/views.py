from django.shortcuts import render
from .models import Meal
from .forms import MealForm

def index(request):
    meals = Meal.objects.all()
    context = {'meals': meals}
    return render(request, 'index.html', context)

def insert_meal(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('calories'):
            save_meal = Meal()

            save_meal.name = request.POST.get('name')
            save_meal.calories = request.POST.get('calories')
            save_meal.save()
            message = "Meal saved successfully!"
            return render(request, 'insert.html', {'message': message})
    else:
        return render(request, 'insert.html')

def edit_meal(request, id):
    meal = Meal.objects.get(id=id)
    return render(request, 'edit.html', {'meal': meal})

def update_meal(request, id):
    meal = Meal.objects.get(id=id)
    form = MealForm(request.POST, instance=meal)
    if form.is_valid():
        form.save()
        message = "Meal updated successfully!"
        return render(request, 'edit.html', {'meal': meal, 'message': message})

def delete_meal(request, id):
    meal = Meal.objects.get(id=id)
    meal.delete()
    meals = Meal.objects.all()
    return render(request, 'index.html', {'meals': meals})