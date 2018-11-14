
# Create your views here.
from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View
from .forms import UsersForm, PasswordForm
from .models import Users, Password
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
        }
        return render(
            request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(
            request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
                'form': bound_form,
                'post': post,
            }
            return render(
                request,
                self.template_name,
                context)
