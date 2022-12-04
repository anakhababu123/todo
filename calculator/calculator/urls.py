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
from operations.views  import AddView, CheckView,MultiplicationView,SubstractionView,ExponentView,FactorialView,NumcheckView,PrimeView


urlpatterns = [
    path('superuser/', admin.site.urls),
    path("operations/add",AddView.as_view()),
    path("operations/sub",SubstractionView.as_view()),
    path("operations/exp",ExponentView.as_view()),
    path("operations/mul",MultiplicationView.as_view()),
    path("operations/numcheck",NumcheckView.as_view()),
    path("operations/prime",PrimeView.as_view()),
    path("operations/fact",FactorialView.as_view()),
    path("operations/check",CheckView.as_view())



]
