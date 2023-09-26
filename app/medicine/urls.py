from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("medicine/", views.MedicineListView.as_view(), name="list"),
    path("medicine/register/", views.MedicineRegisterView.as_view(), name="register"),
    path("medicine/detail", views.MedicineDetailView.as_view(), name="detail"),
    path("medicine/search", views.MedicineSearchView.as_view(), name="search"),
]
