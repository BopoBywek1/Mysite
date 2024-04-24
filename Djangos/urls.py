"""
URL configuration for Djangos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from Djangos import settings
from myop.views import index_page,registra_page,avtoriz_page,film_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_page, name='Main'),
    path('Registra/',registra_page, name='Registra'),
    path('Avtoriz/',avtoriz_page, name='Avtoriz'),
    path('Film/<int:ID>/',film_page, name='Film')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

