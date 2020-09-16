from django.urls import path

from . import views

app_name = "meals"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("plan/", views.PlanView.as_view(), name="plan"),
]
