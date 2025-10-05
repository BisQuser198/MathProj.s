"""
URL configuration for Math_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Factorial.views import factorial_view, factorial_template_view 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('factorial/<n>/', factorial_view), # need to add the comma after
    path('template/<n>', factorial_template_view), # the <n> is a variable which needs to be matched in html, see app_name/template --> views.py
]
