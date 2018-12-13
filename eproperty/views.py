
# Create your views here.
import datetime
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View
from .forms import UsersForm, PasswordForm, RoleCodeForm, PermissionTypeForm, RolePermissionForm, RolePermissionDetailForm, \
    UserRoleForm, LoginForm, ChangePasswordForm,CountryForm, ProvinceForm, CityForm, PropertyCategoryForm, PropertySectorForm,\
    PropertyFacingForm, PropertyImagesForm, PropertyForm, SignUpForm, AdvertisementForm, SearchForm, PasswordFormForPersonalUpdate
from .models import Users, Password, RoleCode, PermissionType, RolePermission, RolePermissionDetail, UserRole, Country, \
    Province, City, PropertyCategory, Property_Sector, Property_Facing, Property, PropertyImages, Advertisement
from django.forms import modelformset_factory, inlineformset_factory

from django.core.mail import send_mail
from django.conf import settings

def home(request):
    return render(request, 'eproperty/home.html')

def about(request):
    return render(request, 'eproperty/about.html')

def sportEquip(request):
    return render(request, 'eproperty/sportequip.html')

def properties(request):
    return render(request, 'eproperty/properties.html')

def contact(request):
    return render(request, 'eproperty/contact.html')

def advanceSearch(request):
    return render(request, 'eproperty/SearchAdvance.html')

def advertisement(request):
    propIDs = Advertisement.objects.filter(advStartDate__lte=datetime.date.today()).filter(advEndDate__gte=datetime.date.today()).order_by('-adv_ID').values('propertyID')

    #prop = Property.objects.filter(propertyID__in=propIDs)
    prop = Property.objects.filter(propertyID__in=propIDs).prefetch_related('propImg').all()


    # print(prop)
    # for p in prop:
    #
    #     child = p.propImg.all()
    #     print(child)
    #





    context = {
        'property_list': prop
    }


    return render(request, 'eproperty/Advertisement.html', context)

def dashboard(request):
    if request.session.get('userType', 'mini') == 'admin':
        return redirect('eproperty:Users_List')
    else:
        return redirect('eproperty:Advertisement_list')

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

            if user and user.isActive:

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


                request.session['userType'] = userRole.roleCode_ID.name
                request.session['userID'] = user.user_ID.user_ID

                if user.passwordMustChanged:
                    return render(
                        request,
                        'eproperty/changePassword.html',
                        {'formP': self.chpaswd_form_class(),
                         'userName': userName})


                # sesseion object created
                #request.session['pass_obj'] = user



                if 'admin' == userRole.roleCode_ID.name:
                    return redirect('eproperty:Users_List')
                else:
                    return redirect('eproperty:Advertisement_list')




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
                passwordM = Password.objects.get(userName=userName)
                passwordM.encryptedPassword = password
                passwordM.passwordMustChanged = False
                passwordM.save()

                #print(request.session.get('userType', 'mini'))

                if request.session.get('userType', 'mini') == 'admin':
                    return redirect('eproperty:Users_List')
                else:
                    return redirect('eproperty:Advertisement_list')


            else:
                errorMSG = 'Password Mismatch. Try Again'
                return render(request, 'eproperty/changePassword.html',
                              {'formP': self.form_class(), 'userName': userName, 'errorMSG': errorMSG})

        return redirect('eproperty:login')


class signUp(View):
    form_class = SignUpForm
    template_name = 'eproperty/SignUp.html'

    signup_form_class = LoginForm
    signup_template_name = 'eproperty/login.html'

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




        user = Password.objects.filter(userName = userName)

        if user:
            errorMSG = "User Name Already exist."

            return render(
                request,
                self.template_name,
                {'formP': bound_formP, 'errorMSG': errorMSG})





        if bound_formP.is_valid():
            userModel = Users(firstName=firstName, lastName=lastName, email=email)
            userModel.save()
            passwordModal = Password(userName=userName, encryptedPassword=userName, userAccountExpiryDate=(datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))
            passwordModal.user_ID_id = userModel.user_ID
            passwordModal.save()
            #print((datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))

            subject = 'New User Sign Up Request: '+userName
            message = "New User has requested to Sign-Up: Real Estate Site\nUser details are as follows:-\n\n"
            message += "User Name: "+userName+"\nFirst Name: "+firstName+"\nLast Name: "+lastName+"\nEmail: "+email
            message += "\n\n Kindly Activate & Assign Role to this user through your portal."

            sendEmailToAdmin(subject, message)

            errorMSG = 'You have SignUp. You will shortly receive an email from the Admin'

            return render(
                request,
                self.signup_template_name,
                {'formL': self.signup_form_class(), 'errorMSG': errorMSG})
            return redirect('eproperty:login')

        return redirect('eproperty:SignUp')

def reset(request):
    return render(request, 'eproperty/reset.html')


def sendEmailToAdmin(subject, message):
    email_from = settings.EMAIL_DUMMY
    recipient_list = ['shah13yWindsor@gmail.com']
    send_mail( subject, message, email_from, recipient_list)

def sendEmailToUser(subject, message, recipient):
    email_from = settings.EMAIL_DUMMY
    recipient_list = [recipient]
    send_mail( subject, message, email_from, recipient_list)

class activateUser(View):
    def get(self, request, uID):

        passwordM = Password.objects.get(password_ID=uID)

        subject = 'Welcome to your new Real Estate Account: ' + passwordM.userName
        message = "Thank you for creating a Real Estate Account. Here is some advice to get started with your account.\n\n"
        message += "You User name: "+passwordM.userName+"\nYour Temporary Password is: "+passwordM.encryptedPassword
        message += "\n\n You can now login to your account by filling above details"
        sendEmailToUser(subject, message, passwordM.user_ID.email)




        passwordM.isActive = True
        passwordM.save()

        return redirect('eproperty:Users_List')

class resetUserPassword(View):
    form_class = UsersForm
    form_class_password = PasswordForm
    template_name = 'eproperty/UsersUpdate_form.html'

    def get(self, request, uID):
        passwordM = Password.objects.get(password_ID=uID)
        passwordM.passwordMustChanged = True
        passwordM.save()

        if request.session.get('userType', 'mini') == 'admin':
            return redirect('eproperty:Users_List')
        else:
            userM = get_object_or_404(Users, user_ID=request.session.get('userID', 1))
            passM = get_object_or_404(Password, user_ID=userM)

            context = {
                'formU': self.form_class(
                    instance=userM),
                'formP': self.form_class_password(instance=passM),
                'userM': userM,
                'passM': passM,
                'errorMSG': "You will be asked to change your password in your next Login."
            }

            return render(
                request,
                self.template_name,
                context)

class logoutUser(View):
    def get(self, request):
        print("logout")
        del request.session['userID']
        del request.session['userType']

        return redirect('eproperty:login')



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

        user = Password.objects.filter(userName=bound_formP['userName'].value())

        if user:
            errorMSG = "User Name Already exist."

            return render(
                request,
                self.template_name,
                {'formU': bound_formU, 'formP': bound_formP, 'errorMSG': errorMSG})



        if bound_formU.is_valid():
            new_post = bound_formU.save()

            if bound_formP.is_valid():
                passwordModal = Password(userName=bound_formP['userName'].value(), userAccountExpiryDate=bound_formP['userAccountExpiryDate'].value(), user_ID=new_post, encryptedPassword=bound_formP['userName'].value())
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
            {'password_list': Password.objects.all().order_by('-password_ID')})





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
            'userM': userM,
            'passM': passM
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
                'passM': passM
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

        userIds = UserRole.objects.all().values('user_ID')

        form = self.form_class()
        form.fields['user_ID'].queryset = Users.objects.all().exclude(
            user_ID__in=userIds)


        return render(
            request,
            self.template_name,
            {'formU': form})

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

        form = self.form_class(instance=userM)
        form.fields['user_ID'].queryset = Users.objects.filter(user_ID=userM.user_ID.user_ID)

        context = {
            'formU': form,
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
        form = self.form_class()
        form.fields['propertyID'].queryset = Property.objects.filter(user_ID=request.session.get('userID', 1))
        return render(
            request,
            self.template_name,
            {'formU': form})

    def post(self, request):
        bound_formU = self.form_class(request.POST, request.FILES)

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

        if request.session.get('userType', 'mini') == 'admin':
            userID= 1
        else:
            userID = request.session.get('userID', 1)

        propIDs = Property.objects.filter(user_ID=userID).order_by('-propertyID').values('propertyID')

        #print(propIDs)



        return render(
            request,
            'eproperty/PropertyImages_list.html',
            {'propertyImages_list': PropertyImages.objects.filter(propertyID__in=propIDs).order_by('-propertyImageID')})


class PropertyImagesUpdate(View):
    form_class = PropertyImagesForm
    template_name = 'eproperty/PropertyImagesUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(PropertyImages, propertyImageID=uID)

        form = self.form_class(instance=userM)
        form.fields['propertyID'].queryset = Property.objects.filter(user_ID=request.session.get('userID', 1))

        context = {
            'formU': form,
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(PropertyImages, propertyImageID=uID)
        bound_formU = self.form_class(
            request.POST, request.FILES, instance=userM)
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

        #self.form_class.user_ID = request.session.get('userID', 1)

        return render(
            request,
            self.template_name,
            {'formU': self.form_class(initial={'user_ID': request.session.get('userID', 1)})})

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

        if request.session.get('userType', 'mini') == 'admin':
            userID= 1
        else:
            userID = request.session.get('userID', 1)


        return render(
            request,
            'eproperty/Property_list.html',
            {'property_list': Property.objects.filter(user_ID=userID).order_by('-propertyID')})


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




class AdvertisementCreate(View):
    form_class = AdvertisementForm
    template_name = 'eproperty/Advertisement_form.html'

    def get(self, request):

        propIds = Advertisement.objects.filter(user_ID=request.session.get('userID', 1)).values('propertyID')

        form = self.form_class(initial={'user_ID': request.session.get('userID', 1)})
        form.fields['propertyID'].queryset = Property.objects.filter(user_ID=request.session.get('userID', 1)).exclude(propertyID__in=propIds)

        return render(
            request,
            self.template_name,
            {'formU': form})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Advertisement_list')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})


class AdvertisementList(View):
    def get(self, request):

        return render(
            request,
            'eproperty/Advertisement_list.html',
            {'advertisement_list': Advertisement.objects.filter(user_ID=request.session.get('userID', 1)).order_by('-advStartDate')})


class AdvertisementUpdate(View):
    form_class = AdvertisementForm
    template_name = 'eproperty/AdvertisementUpdate_form.html'

    def get(self, request, uID):
        userM = get_object_or_404(Advertisement, adv_ID=uID)
        form = self.form_class(instance=userM)
        form.fields['propertyID'].queryset = Property.objects.filter(propertyID=userM.propertyID.propertyID)

        context = {
            'formU': form,
            'userM': userM
        }
        return render(
            request, self.template_name, context)

    def post(self,request, uID):
        userM = get_object_or_404(Advertisement, adv_ID=uID)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('eproperty:Advertisement_list')
        else:
            context = {
                'formU': bound_formU,
                'userM': userM,
            }
            return render(
                request,
                self.template_name,
                context)


class AdvertisementDelete(View):

    def get(self, request, uID):
        userM = get_object_or_404(Advertisement, adv_ID=uID)
        userM.delete()
        return redirect('eproperty:Advertisement_list')

########################################################################################################


class Search(View):
    form_class = SearchForm
    template_name = 'eproperty/Search.html'

    signup_form_class = LoginForm
    signup_template_name = 'eproperty/login.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formP': self.form_class()})

    def post(self, request):

        bound_formP = self.form_class(request.POST)

        category = bound_formP['category'].value()
        sector = bound_formP['sector'].value()
        country = bound_formP['country'].value()
        province = bound_formP['province'].value()
        city = bound_formP['city'].value()
        #askingPrice = bound_formP['askingPrice'].value()

        #print(askingPrice)

        prop = Property.objects.all()

        if category:
            prop = prop.filter(propertyCategory=category)
        if sector:
            prop = prop.filter(propertySector=sector)
        if country:
            prop = prop.filter(propertyCountry=country)
        if province:
            prop = prop.filter(propertyProvince=province)
        if city:
            prop = prop.filter(propertyCity=city)


        print(prop)

        return render(
            request,
            self.template_name,
            {'formP': bound_formP,
             'propertySearchList': prop
             })

########################################################################################################


class PersonalDetailUpdate(View):
    form_class = UsersForm
    form_class_password = PasswordFormForPersonalUpdate
    template_name = 'eproperty/UsersUpdate_form.html'

    def get(self, request):
        userM = get_object_or_404(Users, user_ID=request.session.get('userID', 1))
        passM = get_object_or_404(Password, user_ID=userM)
        context = {
            'formU': self.form_class(
                instance=userM),
            'formP': self.form_class_password(instance=passM),
            'userM': userM,
            'passM': passM
        }
        return render(
            request, self.template_name, context)

    def post(self,request):
        userM = get_object_or_404(Users, user_ID=request.session.get('userID', 1))
        passM = get_object_or_404(Password, user_ID=userM)
        bound_formU = self.form_class(
            request.POST, instance=userM)
        bound_formP = self.form_class_password(
            request.POST, instance=passM)
        if bound_formU.is_valid():
            new_post = bound_formU.save()
            if bound_formP.is_valid():
                bound_formP.save()

            userM = get_object_or_404(Users, user_ID=request.session.get('userID', 1))
            passM = get_object_or_404(Password, user_ID=userM)

            context = {
                'formU': self.form_class(
                    instance=userM),
                'formP': self.form_class_password(instance=passM),
                'userM': userM,
                'passM': passM,
                'errorMSG': "You have successfully updated your Personal Details"
            }

            return render(
                request,
                self.template_name,
                context)

        else:
            context = {
                'formU': bound_formU,
                'formP': bound_formP,
                'userM': userM,
                'passM': passM
            }
            return render(
                request,
                self.template_name,
                context)

########################################################################################################

class SearchAd(View):
    template_name = 'eproperty/SearchAdvertisement.html'

    def get(self, request,uID):
        print("here")
        prop = Property.objects.filter(propertyID=uID).prefetch_related('propImg').all()
        return render(
            request,
            self.template_name,
            {'property_list': prop})
