from django.urls import path, include
from .views import function_view

app_name = "function"

## URL mic
urlpatterns = [
    path("", function_view),
]

## 