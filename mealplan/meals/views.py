from random import sample

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Meal


class IndexView(generic.ListView):
    model = Meal
    context_object_name = "meals"


class DetailView(generic.UpdateView):
    model = Meal
    fields = ["name"]


class PlanView(generic.ListView):
    model = Meal
    context_object_name = "plan"
    template_name = "meals/plan_list.html"

    def get_queryset(self):
        meals = Meal.objects.all()
        return sample([m for m in meals], 7)
