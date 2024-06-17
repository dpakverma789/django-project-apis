

from django.urls import path
from questionbank import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/', views.question_bank, name='question-bank')
]
