from django.urls import path

from . import views

# Define a namespace to use url namespace:name
app_name = "vehicle_management"

urlpatterns = [
    path("", views.IndexView.as_view(), name="car-index"),
    path("cars/<int:pk>", views.CarDetailsView.as_view(), name="car-details"),
    path("cars/create", views.CarCreateView.as_view(), name="car-create"),
    path("cars/delete/<int:pk>", views.car_delete, name="car-delete"),
    path("cars/update/<int:pk>", views.CarUpdateView.as_view(), name="car-update"),
]
