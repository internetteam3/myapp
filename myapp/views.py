
# Create your views here.
import datetime
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View
from .forms import UsersForm, PasswordForm, RoleCodeForm, PermissionTypeForm, RolePermissionForm, RolePermissionDetailForm, UserRoleForm, LoginForm, ChangePasswordForm
from .models import Users, Password, RoleCode, PermissionType, RolePermission, RolePermissionDetail, UserRole
from django.forms import modelformset_factory, inlineformset_factory


def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def sportEquip(request):
    return render(request, 'myapp/sportequip.html')

def properties(request):
    return render(request, 'myapp/properties.html')

class login(View):
    form_class = LoginForm
    chpaswd_form_class = ChangePasswordForm
    template_name = 'myapp/login.html'

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
            user = Password.objects.filter(userName = userName, encryptedPassword = password)

            if user:
                print(user)
                return redirect('myapp:Users_List')

            # userModel = Users(firstName="",lastName="",email="")
            # new_post = userModel.save()
            # passwordModal = Password(userName = userName,
            #                          userAccountExpiryDate = (datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'),
            #                          user_ID=new_post)
            # print((datetime.datetime.now() + datetime.timedelta(days=10 * 365)).strftime('%Y-%m-%d'))
            return render(
                request,
                'myapp/changePassword.html',
                {'formP': self.chpaswd_form_class(),
                 'userName':userName})

        else:
            return render(
                request,
                self.template_name,
                {'formL': bound_formL})


class changePassword(View):
    form_class = ChangePasswordForm
    template_name = 'myapp/changePassword.html'

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
                return redirect('myapp:Users_List')

        return redirect('myapp:login')

def reset(request):
    return render(request, 'myapp/reset.html')

######################################################################################################################

class UsersCreate(View):
    form_class = UsersForm
    form_class_password = PasswordForm
    template_name = 'myapp/Users_form.html'

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

            return redirect('myapp:Users_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU, 'formP': bound_formP})



class UsersList(View):

    def get(self, request):
        return render(
            request,
            'myapp/Users_list.html',
            {'users_list': Users.objects.all().order_by('-user_ID')})


class UsersUpdate(View):
    form_class = UsersForm
    form_class_password = PasswordForm
    template_name = 'myapp/UsersUpdate_form.html'

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
            return redirect('myapp:Users_List')
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
        return redirect('myapp:Users_List')

#######################################################################################################################

class RoleCodeCreate(View):
    form_class = RoleCodeForm
    template_name = 'myapp/RoleCode_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('myapp:RoleCode_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class RoleCodeList(View):

    def get(self, request):
        return render(
            request,
            'myapp/RoleCode_list.html',
            {'roleCode_list': RoleCode.objects.all().order_by('-roleCode_ID')})


class RoleCodeUpdate(View):
    form_class = RoleCodeForm
    template_name = 'myapp/RoleCodeUpdate_form.html'

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

            return redirect('myapp:RoleCode_List')
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
        return redirect('myapp:RoleCode_List')


#######################################################################################################################

class PermissionTypeCreate(View):
    form_class = PermissionTypeForm
    template_name = 'myapp/PermissionType_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('myapp:PermissionType_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class PermissionTypeList(View):

    def get(self, request):
        return render(
            request,
            'myapp/PermissionType_list.html',
            {'permissionType_list': PermissionType.objects.all().order_by('-permission_ID')})


class PermissionTypeUpdate(View):
    form_class = PermissionTypeForm
    template_name = 'myapp/PermissionTypeUpdate_form.html'

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

            return redirect('myapp:PermissionType_List')
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
        return redirect('myapp:PermissionType_List')


#######################################################################################################################

#######################################################################################################################

class RolePermissionCreate(View):
    form_class = RolePermissionForm
    template_name = 'myapp/RolePermission_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('myapp:RolePermission_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class RolePermissionList(View):

    def get(self, request):
        return render(
            request,
            'myapp/RolePermission_list.html',
            {'rolePermission_list': RolePermission.objects.all().order_by('-rolePermission_ID')})


class RolePermissionUpdate(View):
    form_class = RolePermissionForm
    template_name = 'myapp/RolePermissionUpdate_form.html'

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

            return redirect('myapp:RolePermission_List')
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
        return redirect('myapp:RolePermission_List')


#######################################################################################################################

#######################################################################################################################

class RolePermissionDetailCreate(View):
    form_class = RolePermissionDetailForm
    template_name = 'myapp/RolePermissionDetail_form.html'

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

        return redirect('myapp:RolePermissionDetail_List')







class RolePermissionDetailList(View):

    def get(self, request):
        return render(
            request,
            'myapp/RolePermissionDetail_list.html',
            {'rolePermission_list': RolePermissionDetail.objects.all().order_by('-rolePermissionDetail_ID')})


class RolePermissionDetailUpdate(View):
    form_class = RolePermissionDetailForm
    template_name = 'myapp/RolePermissionDetailUpdate_form.html'

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

            return redirect('myapp:RolePermissionDetail_List')
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
        return redirect('myapp:RolePermissionDetail_List')


#######################################################################################################################
#######################################################################################################################

class UserRoleCreate(View):
    form_class = UserRoleForm
    template_name = 'myapp/UserRole_form.html'

    def get(self, request):
        return render(
            request,
            self.template_name,
            {'formU': self.form_class()})

    def post(self, request):
        bound_formU = self.form_class(request.POST)


        if bound_formU.is_valid():
            new_post = bound_formU.save()

            return redirect('myapp:UserRole_List')
        else:
            return render(
                request,
                self.template_name,
                {'formU': bound_formU})



class UserRoleList(View):

    def get(self, request):
        return render(
            request,
            'myapp/UserRole_list.html',
            {'userRole_list': UserRole.objects.all().order_by('-userRole_ID')})


class UserRoleUpdate(View):
    form_class = UserRoleForm
    template_name = 'myapp/UserRoleUpdate_form.html'

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

            return redirect('myapp:UserRole_List')
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
        return redirect('myapp:UserRole_List')


#######################################################################################################################



