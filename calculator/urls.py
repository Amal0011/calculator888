"""calculator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from operation import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addition/',views.AdditionView.as_view(),name="add"),
    path('subtraction/',views.SubtractionView.as_view(),name="sub"),
    path('amstrong/',views.AmstrongView.as_view(),name="amstrong"),
    path('evens/',views.EvenNumbersView.as_view(),name="evens"),
    path('health/',views.HealthView.as_view(),name="health"),
    path('degtofaren/',views.TempView.as_view(),name="degtofaren"),
    path('exponent/',views.ExponentView.as_view(),name="exponent"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('login2/',views.Login2View.as_view(),name="login2"),
    path('',views.HomeView.as_view(),name="index"),
]
