from django import forms

from .models import Users, Password


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email']
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'single-input'}),
            'lastName': forms.TextInput(attrs={'class': 'single-input'}),
            'email':forms.EmailInput(attrs={'class': 'single-input'})
        }

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['userName', 'encryptedPassword', 'userAccountExpiryDate']
        widgets = {
            'userName': forms.TextInput(attrs={'class': 'single-input'}),
            'encryptedPassword': forms.PasswordInput(attrs={'class': 'single-input'})

        }
