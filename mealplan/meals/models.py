from datetime import date, timedelta

from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    """
    Common behaviour goes here!
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Meal(BaseModel):
    """
    Basic Model for a Meal
    """

    name = models.CharField(max_length=256)

    difficulty = models.IntegerField()
    healthiness = models.IntegerField()

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(difficulty__range=(0, 10)),
                name="difficulty_between_0_and_10",
            ),
            models.CheckConstraint(
                check=models.Q(healthiness__range=(0, 10)),
                name="healthiness_between_0_and_10",
            ),
        ]

        ordering = [
            "name",
        ]

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("meals:detail", kwargs={"pk": self.pk})


class MealPlan(BaseModel):
    """
    A list of meals, with a start date, and an order
    """

    start_date = models.DateField()
    meals = models.ManyToManyField(Meal, through="MealPlanOrder")

    class Meta:
        ordering = ["start_date"]

    def __str__(self):
        dates = self.dates()

        meal_strs = []
        for d, meal in zip(dates, self.meals.all()):
            meal_str = f"{d} - {meal}"
            meal_strs.append(meal_str)

        return "\n".join(meal_strs)

    def dates(self):
        meal_count = self.meals.count()
        return [self.start_date + timedelta(days=d) for d in range(meal_count)]

    def days(self):
        return [d.strftime("%A") for d in self.dates()]


class MealPlanOrder(models.Model):
    """
    The through table for Meal Plan <==> Meal relationship
    """

    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

    order = models.PositiveIntegerField()
