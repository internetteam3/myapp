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
from eproperty import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

app_name = 'eproperty'
urlpatterns = [

                  path(r'', views.home,name='home'),

                  path(r'about', views.about, name='about'),

                  path(r'sportEquip', views.sportEquip, name='sportEquip'),

                  path(r'properties', views.properties, name='properties'),

                  url(r'^login/$', views.login.as_view(),
                      name='login'),

                  url(r'^logout/$', views.logoutUser.as_view(),
                      name='Logout'),


                  url(r'^changePassword/$', views.changePassword.as_view(),
                      name='changePassword'),

                  url(r'^signUp/$', views.signUp.as_view(),
                      name='SignUp'),

                  url(r'^activateUser/(?P<uID>\d+)$', views.activateUser.as_view(),
                      name='ActivateUser'),

                  url(r'^resetUserPassword/(?P<uID>\d+)$', views.resetUserPassword.as_view(),
                      name='ResetUserPassword'),

                  url(r'^search/$', views.Search.as_view(),
                      name='Search'),

                  url(r'^personalDetailUpdate/$',
                      views.PersonalDetailUpdate.as_view(),
                      name='PersonalDetail_update'),

                  url(r'^advertisement/$', views.advertisement,
                      name='Advertisement'),



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








#country

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



    #province

                  url(r'^provinceCreate/$',
                      views.ProvinceCreate.as_view(),
                      name='Province_create'),

                  url(r'^provinceList/$',
                      views.ProvinceList.as_view(),
                      name='Province_list'),

                  url(r'^provinceUpdate/(?P<uID>\d+)$',
                      views.ProvinceUpdate.as_view(),
                      name='Province_update'),

                  url(r'^provinceDelete/(?P<uID>\d+)$',
                      views.ProvinceDelete.as_view(),
                      name='Province_delete'),





# city

                  url(r'^cityCreate/$',
                      views.CityCreate.as_view(),
                      name='City_create'),

                  url(r'^cityList/$',
                      views.CityList.as_view(),
                      name='City_list'),

                  url(r'^cityUpdate/(?P<uID>\d+)$',
                      views.CityUpdate.as_view(),
                      name='City_update'),

                  url(r'^cityDelete/(?P<uID>\d+)$',
                      views.CityDelete.as_view(),
                      name='City_delete'),




# propertyCategory

                  url(r'^propertyCategoryCreate/$',
                      views.PropertyCategoryCreate.as_view(),
                      name='PropertyCategory_create'),

                  url(r'^propertyCategoryList/$',
                      views.PropertyCategoryList.as_view(),
                      name='PropertyCategory_list'),

                  url(r'^propertyCategoryUpdate/(?P<uID>\d+)$',
                      views.PropertyCategoryUpdate.as_view(),
                      name='PropertyCategory_update'),

                  url(r'^propertyCategoryDelete/(?P<uID>\d+)$',
                      views.PropertyCategoryDelete.as_view(),
                      name='PropertyCategory_delete'),


# propertySector

                  url(r'^propertySectorCreate/$',
                      views.PropertySectorCreate.as_view(),
                      name='PropertySector_create'),

                  url(r'^propertySectorList/$',
                      views.PropertySectorList.as_view(),
                      name='PropertySector_list'),

                  url(r'^propertySectorUpdate/(?P<uID>\d+)$',
                      views.PropertySectorUpdate.as_view(),
                      name='PropertySector_update'),

                  url(r'^propertySectorDelete/(?P<uID>\d+)$',
                      views.PropertySectorDelete.as_view(),
                      name='PropertySector_delete'),



# propertyFacing

                  url(r'^propertyFacingCreate/$',
                      views.PropertyFacingCreate.as_view(),
                      name='PropertyFacing_create'),

                  url(r'^propertyFacingList/$',
                      views.PropertyFacingList.as_view(),
                      name='PropertyFacing_list'),

                  url(r'^propertyFacingUpdate/(?P<uID>\d+)$',
                      views.PropertyFacingUpdate.as_view(),
                      name='PropertyFacing_update'),

                  url(r'^propertyFacingDelete/(?P<uID>\d+)$',
                      views.PropertyFacingDelete.as_view(),
                      name='PropertyFacing_delete'),




# propertyImages

                  url(r'^propertyImagesCreate/$',
                      views.PropertyImagesCreate.as_view(),
                      name='PropertyImages_create'),

                  url(r'^propertyImagesList/$',
                      views.PropertyImagesList.as_view(),
                      name='PropertyImages_list'),

                  url(r'^propertyImagesUpdate/(?P<uID>\d+)$',
                      views.PropertyImagesUpdate.as_view(),
                      name='PropertyImages_update'),

                  url(r'^propertyImagesDelete/(?P<uID>\d+)$',
                      views.PropertyImagesDelete.as_view(),
                      name='PropertyImages_delete'),



# property

                  url(r'^propertyCreate/$',
                      views.PropertyCreate.as_view(),
                      name='Property_create'),

                  url(r'^propertyList/$',
                      views.PropertyList.as_view(),
                      name='Property_list'),

                  url(r'^propertyUpdate/(?P<uID>\d+)$',
                      views.PropertyUpdate.as_view(),
                      name='Property_update'),

                  url(r'^propertyDelete/(?P<uID>\d+)$',
                      views.PropertyDelete.as_view(),
                      name='Property_delete'),






# adv

                  url(r'^advertisementCreate/$',
                      views.AdvertisementCreate.as_view(),
                      name='Advertisement_create'),

                  url(r'^advertisementList/$',
                      views.AdvertisementList.as_view(),
                      name='Advertisement_list'),

                  url(r'^advertisementUpdate/(?P<uID>\d+)$',
                      views.AdvertisementUpdate.as_view(),
                      name='Advertisement_update'),

                  url(r'^advertisementDelete/(?P<uID>\d+)$',
                      views.AdvertisementDelete.as_view(),
                      name='Advertisement_delete'),








              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


