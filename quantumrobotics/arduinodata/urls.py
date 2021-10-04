from django.urls import path

from . import views 
from .views import IndexListView

app_name='arduinodata'
urlpatterns = [
    path('',IndexListView.as_view(), name='index'),
    path('model/<str:board>/', views.model, name='model'),
    path('registers/<str:model_board>/', views.data, name='arduino-data')
]
