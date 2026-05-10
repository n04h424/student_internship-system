"""
URL configuration for main_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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

from . import views
# go back one level and import the views.py file

urlpatterns =   [
                    path('admin/', admin.site.urls),
                    path('',views.homepage),
                    # when http://127.0.0.1:8000/ has nothing after
                    # go to the views.py of the current level, look for homepage function and carry it out
                    path('about/',views.about)
                    # when http://127.0.0.1:8000/ has 'about/' after
                    # go to the views.py of the current level, look for homepage function and carry it out
                ]
