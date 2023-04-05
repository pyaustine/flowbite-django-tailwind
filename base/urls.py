from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('welcome/', views.welcome, name='welcome'),
    path('survey/', views.survey, name='survey'),
    path('survey/predictor/', views.predictor, name='predictor'),
]
