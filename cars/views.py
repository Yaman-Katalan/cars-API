from django.shortcuts import render
from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

# Create your views here.
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


