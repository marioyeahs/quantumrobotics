from django.shortcuts import render
from django.views.generic import ListView
from .models import Arduino
# Create your views here.

class IndexListView(ListView):
    model=Arduino
    template_name='./index.html'
    def get_queryset(self):
        return Arduino.objects.all()

