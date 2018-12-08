
# Create your views here.
import datetime
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View
from .forms import UsersForm, PasswordForm, RoleCodeForm, PermissionTypeForm, RolePermissionForm, RolePermissionDetailForm, \
    UserRoleForm, LoginForm, ChangePasswordForm,CountryForm, ProvinceForm, CityForm, PropertyCategoryForm, PropertySectorForm,\
    PropertyFacingForm, PropertyImagesForm, PropertyForm, SignUpForm
from .models import Users, Password, RoleCode, PermissionType, RolePermission, RolePermissionDetail, UserRole, Country, \
    Province, City, PropertyCategory, Property_Sector, Property_Facing, Property, PropertyImages
from django.forms import modelformset_factory, inlineformset_factory


def home(request):
    return render(request, 'eproperty/home.html')

def about(request):
    return render(request, 'eproperty/about.html')

def sportEquip(request):
    return render(request, 'eproperty/sportequip.html')

def properties(request):
    return render(request, 'eproperty/properties.html')

class login(View):
    form_class = LoginForm
    chpaswd_form_class = ChangePasswordForm
    template_name = 'eproperty/login.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formL': self.form_class()})

    def post(self, request):

        bound_formL = self.form_class(request.POST)
        userName = bound_formL['user_name'].value()
        password = bound_formL['password'].value()

        if bound_formL.is_valid():

            # user = get_object_or_404(Password, userName=userName)
            # user, created = Password.objects.get_or_create(userName = userName, encryptedPassword = password)
            #user = Password.objects.filter(userName = userName, encryptedPassword = password)
            #user = Password.objects.filter(userName=userName, encryptedPassword=password)

            try:
                user = Password.objects.get(userName=userName, encryptedPassword=password)
            except Password.DoesNotExist:
                user = None

            if user:

                try:
                    userRole = UserRole.objects.get(user_ID=user.user_ID)
                except UserRole.DoesNotExist:
                    userRole = None

                if userRole:
                    print(userRole.roleCode_ID.name)
                else:
                    errorMSG = 'No Role Assigned by the Admin'

                    return render(
                        request,
                        self.template_name,
                        {'formL': self.form_class(), 'errorMSG': errorMSG})


                return redirect('eproperty:Users_List')
            else:
                errorMSG = 'Invalid Login Credentials. Please Try Again'

                return render(
                    request,
                    self.template_name,
                    {'formL': self.form_class(), 'errorMSG': errorMSG})

            # userModel = Users(firstName="",lastName="",email="")
            # new_post = userModel.save()
            # passwordModal = Password(userName = userName,
            #                          userAccountExpiryDate = (datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'),
            #                          user_ID=new_post)
            # print((datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))

            return render(
                request,
                'eproperty/changePassword.html',
                {'formP': self.chpaswd_form_class(),
                 'userName':userName})

        else:
            return render(
                request,
                self.template_name,
                {'formL': bound_formL})


class changePassword(View):
    form_class = ChangePasswordForm
    template_name = 'eproperty/changePassword.html'

    def post(self, request):

        bound_formP = self.form_class(request.POST)
        password = bound_formP['password'].value()
        change_password = bound_formP['reenter_password'].value()
        userName = request.POST['userName']

        if bound_formP.is_valid():

            if password == change_password:
                userModel = Users(firstName=userName, lastName=userName, email=userName+"@gmail.com")
                userModel.save()
                passwordModal = Password(userName = userName,
                                         encryptedPassword = password,
                                         userAccountExpiryDate = (datetime.datetime.now() + datetime.timedelta(
                                             days=10 * 365)).strftime('%Y-%m-%d')
                                         )
                passwordModal.user_ID_id = userModel.user_ID
                passwordModal.save()
                print((datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))
                return redirect('eproperty:Users_List')

        return redirect('eproperty:login')


class signUp(View):
    form_class = SignUpForm
    template_name = 'eproperty/SignUp.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formP': self.form_class()})

    def post(self, request):

        bound_formP = self.form_class(request.POST)

        userName = bound_formP['userName'].value()
        firstName = bound_formP['firstName'].value()
        lastName = bound_formP['lastName'].value()
        email = bound_formP['email'].value()
        encryptedPassword = bound_formP['encryptedPassword'].value()
        reenter_password = bound_formP['reenter_password'].value()

        if encryptedPassword != reenter_password:

            errorMSG = "Password and Confirm Password doesn't match."

            return render(
                request,
                self.template_name,
                {'formP': bound_formP, 'errorMSG': errorMSG})



        user = Password.objects.filter(userName = userName)

        if user:
            errorMSG = "User Name Already used."

            return render(
                request,
                self.template_name,
                {'formP': bound_formP, 'errorMSG': errorMSG})





        if bound_formP.is_valid():
            userModel = Users(firstName=firstName, lastName=lastName, email=email)
            userModel.save()
            passwordModal = Password(userName=userName, encryptedPassword=encryptedPassword, userAccountExpiryDate=(datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))
            passwordModal.user_ID_id = userModel.user_ID
            passwordModal.save()
            print((datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))
            return redirect('eproperty:login')

        return redirect('eproperty:SignUp')

def reset(request):
    return render(request, 'eproperty/reset.html')

######################################################################################################################

class UsersCreate(View):
    form_class = UsersForm
    form_class_password = PasswordForm
    template_name = 'eproperty/Users_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class(), 'formP': self.form_class_password()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)
        bound_formP = self.form_class_password(request.POST)

        if bound_formU.is_valid():
            new_post = bound_formU.save()

            if bound_formP.is_valid():
                passwordModal = Password(userName=bound_formP['userName'].value(), userAccountExpiryDate=bound_formP['userAccountExpiryDate'].value(), user_ID=new_post)
                passwordModal.save()
            else:
                print(bound_formP.errors)

            return redirect('eproperty:Users_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU, 'formP': bound_formP})



class UsersList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/Users_list.html',
            {'users_list': Users.objects.all().order_by('-user_ID')})


class UsersUpdate(View):
    form_class = UsersForm
    form_class_password = PasswordForm
    template_name = 'eproperty/UsersUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Users, user_ID=uID)
        passM = get_object_or_404(Password, user_ID=userM)
        context = {
            'formU': self.form_class(
                instance=userM),
            'formP': self.form_class_password(instance=passM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Users, user_ID=uID)
        passM = get_object_or_404(Password, user_ID=userM)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        bound_formP = self.form_class_password(
            request.POST, instance=passM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()
            if bound_formP.is_valid():
                bound_formP.save()
            return redirect('eproperty:Users_List')
        else:
            context = {
                'formU': bound_formU,
                'formP': bound_formP,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class UsersDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Users, user_ID=uID)
        passM = get_object_or_404(Password, user_ID=userM)
        userM.delete()
        passM.delete()
        return redirect('eproperty:Users_List')

#######################################################################################################################

class RoleCodeCreate(View):
    form_class = RoleCodeForm
    template_name = 'eproperty/RoleCode_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:RoleCode_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class RoleCodeList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/RoleCode_list.html',
            {'roleCode_list': RoleCode.objects.all().order_by('-roleCode_ID')})


class RoleCodeUpdate(View):
    form_class = RoleCodeForm
    template_name = 'eproperty/RoleCodeUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(RoleCode, roleCode_ID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(RoleCode, roleCode_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:RoleCode_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class RoleCodeDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(RoleCode, roleCode_ID=uID)
        userM.delete()
        return redirect('eproperty:RoleCode_List')


#######################################################################################################################

class PermissionTypeCreate(View):
    form_class = PermissionTypeForm
    template_name = 'eproperty/PermissionType_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PermissionType_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class PermissionTypeList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/PermissionType_list.html',
            {'permissionType_list': PermissionType.objects.all().order_by('-permission_ID')})


class PermissionTypeUpdate(View):
    form_class = PermissionTypeForm
    template_name = 'eproperty/PermissionTypeUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(PermissionType, permission_ID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self, request, uID):
        userM = get_object_or_404(PermissionType, permission_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PermissionType_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class PermissionTypeDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(PermissionType, permission_ID=uID)
        userM.delete()
        return redirect('eproperty:PermissionType_List')


#######################################################################################################################

#######################################################################################################################

class RolePermissionCreate(View):
    form_class = RolePermissionForm
    template_name = 'eproperty/RolePermission_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:RolePermission_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class RolePermissionList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/RolePermission_list.html',
            {'rolePermission_list': RolePermission.objects.all().order_by('-rolePermission_ID')})


class RolePermissionUpdate(View):
    form_class = RolePermissionForm
    template_name = 'eproperty/RolePermissionUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(RolePermission, rolePermission_ID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self, request, uID):
        userM = get_object_or_404(RolePermission, rolePermission_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:RolePermission_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class RolePermissionDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(RolePermission, rolePermission_ID=uID)
        userM.delete()
        return redirect('eproperty:RolePermission_List')


#######################################################################################################################

#######################################################################################################################

class RolePermissionDetailCreate(View):
    form_class = RolePermissionDetailForm
    template_name = 'eproperty/RolePermissionDetail_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)

        #RolePermissionFormSet = modelformset_factory(RolePermission, fields=('rolePermission_ID', 'code', 'sysFeature'), extra=0)
        #data = request.POST or None
        #formset = RolePermissionFormSet(data=data, queryset=RolePermission.objects.filter(rolePermission_ID=bound_formU.rolePermission_ID))

        roleCodeM = RoleCode.objects.get(pk=bound_formU['roleCode_ID'].value())
        for rpID in bound_formU['rolePermission_ID'].value():
            rolePermisM = RolePermission.objects.get(pk=rpID)
            rpdM = RolePermissionDetail(roleCode_ID=roleCodeM, rolePermission_ID=rolePermisM)
            rpdM.save()

        return redirect('eproperty:RolePermissionDetail_List')







class RolePermissionDetailList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/RolePermissionDetail_list.html',
            {'rolePermission_list': RolePermissionDetail.objects.all().order_by('-rolePermissionDetail_ID')})


class RolePermissionDetailUpdate(View):
    form_class = RolePermissionDetailForm
    template_name = 'eproperty/RolePermissionDetailUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(RolePermissionDetail, rolePermissionDetail_ID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self, request, uID):
        userM = get_object_or_404(RolePermissionDetail, rolePermissionDetail_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:RolePermissionDetail_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class RolePermissionDetailDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(RolePermissionDetail, rolePermissionDetail_ID=uID)
        userM.delete()
        return redirect('eproperty:RolePermissionDetail_List')


#######################################################################################################################
#######################################################################################################################

class UserRoleCreate(View):
    form_class = UserRoleForm
    template_name = 'eproperty/UserRole_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:UserRole_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class UserRoleList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/UserRole_list.html',
            {'userRole_list': UserRole.objects.all().order_by('-userRole_ID')})


class UserRoleUpdate(View):
    form_class = UserRoleForm
    template_name = 'eproperty/UserRoleUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(UserRole, userRole_ID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self, request, uID):
        userM = get_object_or_404(UserRole, userRole_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:UserRole_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class UserRoleDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(UserRole, userRole_ID=uID)
        userM.delete()
        return redirect('eproperty:UserRole_List')


#######################################################################################################################




#######################################################################################################################

class CountryCreate(View):
    form_class = CountryForm
    template_name = 'eproperty/Country_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Country_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class CountryList(View):

    def get(self, request):
        return render(
            request,
            'eproperty/Country_list.html',
            {'country_list': Country.objects.all().order_by('-countryID')})


class CountryUpdate(View):
    form_class = CountryForm
    template_name = 'eproperty/CountryUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Country, countryID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Country, countryID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Country_List')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class CountryDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Country, countryID=uID)
        userM.delete()
        return redirect('eproperty:Country_List')


#######################################################################################################################



class ProvinceCreate(View):
    form_class = ProvinceForm
    template_name = 'eproperty/Province_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Province_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class ProvinceList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/Province_list.html',
            {'province_list': Province.objects.all().order_by('-provinceID')})


class ProvinceUpdate(View):
    form_class = ProvinceForm
    template_name = 'eproperty/ProvinceUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Province, provinceID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Province, provinceID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Province_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)

class ProvinceDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Province, provinceID=uID)
        userM.delete()
        return redirect('eproperty:Province_list')


#######################################################################################################################

class CityCreate(View):
    form_class = CityForm
    template_name = 'eproperty/City_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:City_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class CityList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/City_list.html',
            {'city_list': City.objects.all().order_by('-cityID')})


class CityUpdate(View):
    form_class = CityForm
    template_name = 'eproperty/CityUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(City, cityID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(City, cityID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:City_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class CityDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(City, cityID=uID)
        userM.delete()
        return redirect('eproperty:City_list')

#######################################################################################################################


class PropertyCategoryCreate(View):
    form_class = PropertyCategoryForm
    template_name = 'eproperty/PropertyCategory_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyCategory_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class PropertyCategoryList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/PropertyCategory_list.html',
            {'propertyCategory_list': PropertyCategory.objects.all().order_by('-propertyCategory')})


class PropertyCategoryUpdate(View):
    form_class = PropertyCategoryForm
    template_name = 'eproperty/PropertyCategoryUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(PropertyCategory, propertyCategory=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(PropertyCategory, propertyCategory=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyCategory_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class PropertyCategoryDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(PropertyCategory, propertyCategory=uID)
        userM.delete()
        return redirect('eproperty:PropertyCategory_list')

#######################################################################################################################



class PropertySectorCreate(View):
    form_class = PropertySectorForm
    template_name = 'eproperty/PropertySector_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertySector_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class PropertySectorList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/PropertySector_list.html',
            {'propertySector_list': Property_Sector.objects.all().order_by('-propertySector')})


class PropertySectorUpdate(View):
    form_class = PropertySectorForm
    template_name = 'eproperty/PropertySectorUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Property_Sector, propertySector=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Property_Sector, propertySector=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertySector_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class PropertySectorDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Property_Sector, propertySector=uID)
        userM.delete()
        return redirect('eproperty:PropertySector_list')

#######################################################################################################################


class PropertyFacingCreate(View):
    form_class = PropertyFacingForm
    template_name = 'eproperty/PropertyFacing_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyFacing_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class PropertyFacingList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/PropertyFacing_list.html',
            {'propertyFacing_list': Property_Facing.objects.all().order_by('-propertyFacing')})


class PropertyFacingUpdate(View):
    form_class = PropertyFacingForm
    template_name = 'eproperty/PropertyFacingUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Property_Facing, propertyFacing=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Property_Facing, propertyFacing=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyFacing_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class PropertyFacingDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Property_Facing, propertyFacing=uID)
        userM.delete()
        return redirect('eproperty:PropertyFacing_list')

#######################################################################################################################


class PropertyImagesCreate(View):
    form_class = PropertyImagesForm
    template_name = 'eproperty/PropertyImages_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)

        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyImages_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class PropertyImagesList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/PropertyImages_list.html',
            {'propertyImages_list': PropertyImages.objects.all().order_by('-propertyImageID')})


class PropertyImagesUpdate(View):
    form_class = PropertyImagesForm
    template_name = 'eproperty/PropertyImagesUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(PropertyImages, propertyImageID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(PropertyImages, propertyImageID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:PropertyImages_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class PropertyImagesDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(PropertyImages, propertyImageID=uID)
        userM.delete()
        return redirect('eproperty:PropertyImages_list')

#######################################################################################################################


class PropertyCreate(View):
    form_class = PropertyForm
    template_name = 'eproperty/Property_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Property_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class PropertyList(View):
    def get(self, request):
        return render(
            request,
            'eproperty/Property_list.html',
            {'property_list': Property.objects.all().order_by('-propertyID')})


class PropertyUpdate(View):
    form_class = PropertyForm
    template_name = 'eproperty/PropertyUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Property, propertyID=uID)
        context = {
            'formU': self.form_class(
                instance=userM),
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Property, propertyID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Property_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class PropertyDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Property, propertyID=uID)
        userM.delete()
        return redirect('eproperty:Property_list')

#######################################################################################################################