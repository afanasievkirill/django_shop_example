from django.urls import path, include
from .views import  test_view


urlpatterns = [
    path('', test_view, name='home')
]
