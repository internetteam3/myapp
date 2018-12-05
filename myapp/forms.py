from django import forms

from .models import Users, Password, RoleCode, PermissionType, RolePermission, RolePermissionDetail, UserRole, Country

class DateInput(forms.DateInput):
    input_type = 'date'
class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['firstName', 'lastName', 'email']
        labels = {
            'firstName':'First Name',
            'lastName':'Last Name'
        }
        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'single-input'}),
            'lastName': forms.TextInput(attrs={'class': 'single-input'}),
            'email':forms.EmailInput(attrs={'class': 'single-input' })
        }

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['userName', 'encryptedPassword', 'userAccountExpiryDate']
        labels = {
            'userName':'User Name',
            'encryptedPassword':'Encrypted Password',
            'userAccountExpiryDate':'Account Expiry Date'
        }
        widgets = {
            'userName': forms.TextInput(attrs={'class': 'single-input'}),
            'encryptedPassword': forms.PasswordInput(attrs={'class': 'single-input'}),
            'userAccountExpiryDate': DateInput()

        }
class RoleCodeForm(forms.ModelForm):
    class Meta:
        model = RoleCode
        fields = ['roleCode_ID', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'single-input'}),
        }

class PermissionTypeForm(forms.ModelForm):
    class Meta:
        model = PermissionType
        fields = ['permission_ID', 'name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'single-input'}),
        }

class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = RolePermission
        fields = ['rolePermission_ID', 'permissionType_ID', 'code', 'sysFeature']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'single-input'}),
            'sysFeature': forms.TextInput(attrs={'class': 'single-input'}),

        }

class RolePermissionDetailForm(forms.ModelForm):
    #rolePermission_ID = forms.ModelMultipleChoiceField(queryset=RolePermission.objects.all())
    rolePermission_ID = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(), queryset=RolePermission.objects.all())

    class Meta:
        model = RolePermissionDetail
        fields = ['rolePermissionDetail_ID', 'roleCode_ID', 'rolePermission_ID']
        widgets = {


        }

class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = ['userRole_ID', 'user_ID', 'roleCode_ID',  'dateAssigned']
        widgets = {
            'dateAssigned': DateInput(),
        }

class LoginForm(forms.Form):
    user_name = forms.CharField(label="",widget = forms.TextInput(attrs={'class': 'single-input','placeholder': 'User Name'}))
    password = forms.CharField(label="",widget = forms.PasswordInput(attrs={'class': 'single-input','placeholder': 'Password'}))

class ChangePasswordForm(forms.Form):
    password = forms.CharField(label="",widget = forms.PasswordInput(attrs={'class': 'single-input','placeholder': 'Enter Password'}))
    reenter_password = forms.CharField(label="",widget = forms.PasswordInput(attrs={'class': 'single-input','placeholder': 're-enter Password'}))


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['countryName']
        widgets = {
            'countryName': forms.TextInput(attrs={'class': 'single-input'}),
        }