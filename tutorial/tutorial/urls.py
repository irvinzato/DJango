"""
URL configuration for tutorial project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mi_app.views import portada, post
from django.conf import settings
from django.conf.urls.static import static   #Para que pueda leer los recursos estaticos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portada, name = "home"), #"name" para asignar un nombre único a cada URL y aprovechar la redirección de URL flexibles
    path('post/<id>', post, name = "post") #indico que en mi URL me daran un atributo "id"
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #Va de la mano con los recursos estaticos
