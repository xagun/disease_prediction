# predictor/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('diabetes/', views.diabetes_prediction, name='diabetes_prediction'),
    path('thyroid/', views.thyroid_prediction, name='thyroid_prediction'),
]


