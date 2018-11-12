from django import forms

from .models import Users,Password


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'


class Password(forms.ModelForm):
    class Meta:
        model = Password
        fields = '__all__'

