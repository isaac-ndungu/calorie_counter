from django.shortcuts import redirect, render
from .models import Meal
from .forms import MealForm
from django.db.models import Sum

def index(request):
    meals = Meal.objects.all()
    
    total_calories = meals.aggregate(total=Sum('calories'))['total'] or 0


    context = {'meals': meals, 'total_calories': total_calories}
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
    
    return redirect('index')

def reset_calories(request):
    Meal.objects.all().delete()
    return redirect('index')