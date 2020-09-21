from random import sample

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Meal, MealPlan


class IndexView(generic.ListView):
    model = Meal
    context_object_name = "meals"


class CreateView(generic.CreateView):
    model = Meal
    fields = ["name", "difficulty", "healthiness"]
    template_name_suffix = "_create_form"


class DetailView(generic.UpdateView):
    model = Meal
    fields = ["name", "difficulty", "healthiness"]
    template_name_suffix = "_update_form"


class MealPlanView(generic.DetailView):
    model = MealPlan
    context_object_name = "plan"
    template_name = "meals/plan_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        obj = self.get_object()
        context["meal_plan"] = zip(obj.days(), obj.meals.all())

        return context


class MealPlansView(generic.ListView):
    model = MealPlan
    context_object_name = "mealplans"
    template_name = "meals/meal_plans_list.html"
