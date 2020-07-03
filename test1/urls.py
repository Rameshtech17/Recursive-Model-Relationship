from django.urls import path

from .views import SchoolAPIView

urlpatterns = [
    path('index/', SchoolAPIView.as_view()),
    ]