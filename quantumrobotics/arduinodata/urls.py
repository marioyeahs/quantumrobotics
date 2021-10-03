from django.urls import path

from . import views 
from .views import IndexListView

app_name='quantumrobotics'
urlpatterns = [
    path('',IndexListView.as_view(), name='index'),
]
