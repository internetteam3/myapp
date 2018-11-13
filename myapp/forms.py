from django import forms

from .models import Users, Password


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email']


class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['userName', 'userAccountExpiryDate']

