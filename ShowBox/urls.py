from django.urls import path
from .views import ShowBoxView
from ShowBox import views

urlpatterns = [
    path('movie/', ShowBoxView.as_view()),
    path('movie/<show_name>', ShowBoxView.as_view()),
    path('movie/<int:id>', ShowBoxView.as_view())
    # path('', views.get, name='get-movie-data')
]