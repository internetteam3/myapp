"""S1_G3_Fall2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

                  path(r'', views.home, name='home'),

                  path(r'about', views.about, name='about'),

                  path(r'sportEquip', views.sportEquip, name='sportEquip'),

                  path(r'properties', views.properties, name='properties'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)