from django.urls import path

from . import views

app_name = "meals"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("create/", views.CreateView.as_view(), name="create"),
    path("plan/", views.PlanView.as_view(), name="plan"),
]
