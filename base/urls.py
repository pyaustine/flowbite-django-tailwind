from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_use, name='terms_of_use'),
=======
    path('about/', views.about, name='about'),
    path('vct/', views.vctPage, name='vct'),
>>>>>>> efcfd5a2036aba545b87caea4764f059b787ff2f
    path('welcome/', views.welcome, name='welcome'),
    path('survey/', views.survey, name='survey'),
    path('survey/predictor/', views.predictor, name='predictor'),
]
