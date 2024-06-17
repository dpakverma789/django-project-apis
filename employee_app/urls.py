

from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from employee_app import views

urlpatterns = [
    # .as_view() needs when we render class based view
    path('', views.EmployeeList.as_view()),
    path('employee/', views.EmployeeList.post_request),
]
