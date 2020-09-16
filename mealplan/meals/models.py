from django.db import models
from django.urls import reverse


class Meal(models.Model):
    name = models.CharField(max_length=256)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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
