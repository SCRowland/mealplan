from random import sample

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Meal


def index(request):
    meals = Meal.objects.all()
    context = {
        "meals": meals,
    }

    return render(request, "meals/index.html", context=context)


def detail(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    context = {
        "meal": meal,
    }

    return render(request, "meals/detail.html", context)


def plan(request):
    meals = Meal.objects.all()

    plan = sample([m for m in meals], 7)
    context = {
        "plan": plan,
    }

    return render(request, "meals/plan.html", context=context)
