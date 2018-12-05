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

                  url(r'^login/$', views.login.as_view(),
                      name='login'),

                  url(r'^changePassword/$', views.changePassword.as_view(),
                      name='changePassword'),

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

                  url(r'^permissionTypeCreate/$',
                      views.PermissionTypeCreate.as_view(),
                      name='PermissionType_create'),

                  url(r'^permissionTypeList/$',
                      views.PermissionTypeList.as_view(),
                      name='PermissionType_List'),

                  url(r'^permissionTypeUpdate/(?P<uID>\d+)$',
                      views.PermissionTypeUpdate.as_view(),
                      name='PermissionType_update'),

                  url(r'^permissionTypeDelete/(?P<uID>\d+)$',
                      views.PermissionTypeDelete.as_view(),
                      name='PermissionType_delete'),

                  url(r'^rolePermissionCreate/$',
                      views.RolePermissionCreate.as_view(),
                      name='RolePermission_create'),

                  url(r'^rolePermissionList/$',
                      views.RolePermissionList.as_view(),
                      name='RolePermission_List'),

                  url(r'^rolePermissionUpdate/(?P<uID>\d+)$',
                      views.RolePermissionUpdate.as_view(),
                      name='RolePermission_update'),

                  url(r'^rolePermissionDelete/(?P<uID>\d+)$',
                      views.RolePermissionDelete.as_view(),
                      name='RolePermission_delete'),

                  url(r'^rolePermissionDetailCreate/$',
                      views.RolePermissionDetailCreate.as_view(),
                      name='RolePermissionDetail_create'),

                  url(r'^rolePermissionDetailList/$',
                      views.RolePermissionDetailList.as_view(),
                      name='RolePermissionDetail_List'),

                  url(r'^rolePermissionDetailUpdate/(?P<uID>\d+)$',
                      views.RolePermissionDetailUpdate.as_view(),
                      name='RolePermissionDetail_update'),

                  url(r'^rolePermissionDetailDelete/(?P<uID>\d+)$',
                      views.RolePermissionDetailDelete.as_view(),
                      name='RolePermissionDetail_delete'),

                  url(r'^userRoleCreate/$',
                      views.UserRoleCreate.as_view(),
                      name='UserRole_create'),

                  url(r'^userRoleList/$',
                      views.UserRoleList.as_view(),
                      name='UserRole_List'),

                  url(r'^userRoleUpdate/(?P<uID>\d+)$',
                      views.UserRoleUpdate.as_view(),
                      name='UserRole_update'),

                  url(r'^userRoleDelete/(?P<uID>\d+)$',
                      views.UserRoleDelete.as_view(),
                      name='UserRole_delete'),










                  url(r'^countryCreate/$',
                      views.CountryCreate.as_view(),
                      name='Country_create'),

                  url(r'^countryList/$',
                      views.CountryList.as_view(),
                      name='Country_List'),

                  url(r'^countryUpdate/(?P<uID>\d+)$',
                      views.CountryUpdate.as_view(),
                      name='Country_update'),

                  url(r'^countryDelete/(?P<uID>\d+)$',
                      views.CountryDelete.as_view(),
                      name='Country_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
