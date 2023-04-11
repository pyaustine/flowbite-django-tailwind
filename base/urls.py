from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vct/', views.vctPage, name='vct'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
    path('terms/', views.terms_of_use, name='terms_of_use'),
    path('welcome/', views.welcome, name='welcome'),
    path('survey/', views.survey, name='survey'),
    path('survey/predictor/', views.predictor, name='predictor'),
]
