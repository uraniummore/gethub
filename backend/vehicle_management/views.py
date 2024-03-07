from django import forms
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView

from vehicle_management.models import Car


class IndexView(generic.ListView):
    template_name = "cars/index.html"
    context_object_name = "cars"

    def get_queryset(self):
        return Car.objects.all()


class CarDetailsView(generic.DetailView):
    template_name = "cars/details.html"
    context_object_name = "car"
    model = Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "title",
            "make",
            "model",
            "year",
            "colour",
            "mileage",
            "vin",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "make": forms.TextInput(attrs={"class": "form-control"}),
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "year": forms.NumberInput(attrs={"class": "form-control"}),
            "colour": forms.TextInput(attrs={"class": "form-control"}),
            "mileage": forms.NumberInput(attrs={"class": "form-control"}),
            "vin": forms.TextInput(attrs={"class": "form-control"}),
        }


class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = "cars/create.html"

    def get_success_url(self):
        return reverse_lazy("car-details", kwargs={"pk": self.object.pk})


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = "cars/create.html"

    def get_success_url(self):
        return reverse_lazy("car-details", kwargs={"pk": self.object.pk})


def car_delete(request, pk):
    if request.method == "DELETE":
        car = get_object_or_404(Car, pk=pk)
        car.delete()

        return JsonResponse({"message": "Car deleted."})
    else:
        return JsonResponse({"message": "Method not allowed."}, status=405)
