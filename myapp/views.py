
# Create your views here.
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View
from .forms import UsersForm, PasswordForm, RoleCodeForm, PermissionTypeForm
from .models import Users, Password, RoleCode, PermissionType
from django.forms import inlineformset_factory


def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def sportEquip(request):
    return render(request, 'myapp/sportequip.html')

def properties(request):
    return render(request, 'myapp/properties.html')

def login(request):
    return render(request, 'myapp/login.html')

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


