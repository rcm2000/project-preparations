"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from pj1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('c1', views.c1, name='c1'),
    path('c1data', views.c1data, name='c1data'),
    path('iots', views.iots, name='iots'),
    path('maps', views.maps, name='maps'),
    path('chart1', views.chart1, name='chart1'),
    path('chart2', views.chart2, name='chart2'),
    path('chart3', views.chart3, name='chart3'),
    path('chart4', views.chart4, name='chart4'),
    # path('chart5', views.chart5, name='chart5'),
    # path('chart5s', views.chart5s, name='chart5s'),
    path('tran', views.tran, name='tran'),
    path('genarating', views.genarating, name='genarating'),
    path('pop', views.pop, name='pop'),
    path('tran', views.tran, name='tran'),
    path('tran', views.tran, name='tran'),

]
