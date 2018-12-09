from django import forms

from .models import Users, Password, RoleCode, PermissionType, RolePermission, RolePermissionDetail, \
    UserRole, Country, Province, City, PropertyCategory, Property_Sector, Property_Facing, PropertyImages, Property, Advertisement


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
        fields = ['userName', 'userAccountExpiryDate', 'isActive']
        labels = {
            'userName':'User Name',
            'userAccountExpiryDate':'Account Expiry Date',
            'isActive':'Active User'
        }
        widgets = {
            'userName': forms.TextInput(attrs={'class': 'single-input'}),
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


class ProvinceForm(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['countryID','provinceName']
        widgets = {

            'provinceName': forms.TextInput(attrs={'class': 'single-input'}),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['cityName','countryName','provinceID']
        widgets = {

            'cityName': forms.TextInput(attrs={'class': 'single-input'}),
        }


class PropertyCategoryForm(forms.ModelForm):
    class Meta:
        model = PropertyCategory
        fields = ['propertyCategoryName']
        widgets = {

            'propertyCategoryName': forms.TextInput(attrs={'class': 'single-input'}),
        }


class PropertySectorForm(forms.ModelForm):
    class Meta:
        model = Property_Sector
        fields = ['propertySectorName']
        widgets = {

            'propertySectorName': forms.TextInput(attrs={'class': 'single-input'}),
        }


class PropertyFacingForm(forms.ModelForm):
    class Meta:
        model = Property_Facing
        fields = ['propertyFacingName']
        widgets = {

            'propertyFacingName': forms.TextInput(attrs={'class': 'single-input'}),
        }


class PropertyImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields = ['propertyID','propertyImage','propertyImageDescription']
        widgets = {
            'propertyImageDescription': forms.TextInput(attrs={'class': 'single-input'}),
        }


class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['propertyTitle','propertyCategory','propertySector','propertyFacing',
                  'propertyCountry','propertyProvince','propertyCity','propertyStreet',
                  'propertyPostalCode','propertyStreetnumber','propertyConstructionDate',
                  'propertyRegistrationDate','propertyNoofHalls','propertyNumberofRooms','propertyNoofBathrooms',
                  'propertyNoofFloors','propertyTotalArea','propertyAskingPrice','propertySellingPrice']
        widgets = {

            'propertyTitle': forms.TextInput(attrs={'class': 'single-input'}),

            'propertyStreet': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyPostalCode': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyStreetnumber': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyConstructionDate': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyRegistrationDate': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyNoofHalls': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyNumberofRooms': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyNoofBathrooms': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyNoofFloors': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyTotalArea': forms.TextInput(attrs={'class': 'single-input'}),
            'propertyAskingPrice': forms.TextInput(attrs={'class': 'single-input'}),
            'propertySellingPrice': forms.TextInput(attrs={'class': 'single-input'}),

        }

class SignUpForm(forms.Form):
    userName = forms.CharField(required=True, label="User Name", widget = forms.TextInput(attrs={'class': 'single-input','placeholder': 'User Name'}))
    firstName = forms.CharField(required=True, label="First Name", widget = forms.TextInput(attrs={'class': 'single-input','placeholder': 'First Name'}))
    lastName = forms.CharField(required=True, label="Last Name", widget = forms.TextInput(attrs={'class': 'single-input','placeholder': 'Last Name'}))
    email = forms.EmailField(required=True, label="Email", widget = forms.TextInput(attrs={'class': 'single-input','placeholder': 'Email'}))


class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['user_ID', 'propertyID','advStartDate', 'advEndDate','advDescription']
        widgets = {
            'advDescription': forms.TextInput(attrs={'class': 'single-input'}),
            'advStartDate': DateInput(),
            'advEndDate': DateInput()
        }

