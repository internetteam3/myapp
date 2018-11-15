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
from django.conf.urls import url

app_name = 'myapp'
urlpatterns = [

                  path(r'', views.home,name='home'),

                  path(r'about', views.about, name='about'),

                  path(r'sportEquip', views.sportEquip, name='sportEquip'),

                  path(r'properties', views.properties, name='properties'),

                  path(r'login', views.login, name='login'),

                  path(r'reset', views.reset, name='reset'),

                  url(r'^usersCreate/$',
                      views.UsersCreate.as_view(),
                      name='Users_create'),

                  url(r'^usersList/$',
                      views.UsersList.as_view(),
                      name='Users_List'),

                  url(r'^usersUpdate/(?P<uID>\d+)$',
                      views.UsersUpdate.as_view(),
                      name='Users_update'),

                  url(r'^usersDelete/(?P<uID>\d+)$',
                      views.UsersDelete.as_view(),
                      name='Users_delete'),

                  url(r'^roleCodeCreate/$',
                      views.RoleCodeCreate.as_view(),
                      name='RoleCode_create'),

                  url(r'^roleCodeList/$',
                      views.RoleCodeList.as_view(),
                      name='RoleCode_List'),

                  url(r'^roleCodeUpdate/(?P<uID>\d+)$',
                      views.RoleCodeUpdate.as_view(),
                      name='RoleCode_update'),

                  url(r'^roleCodeDelete/(?P<uID>\d+)$',
                      views.RoleCodeDelete.as_view(),
                      name='RoleCode_delete'),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
