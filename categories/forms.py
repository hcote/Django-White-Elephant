from django import forms
from .models import Group
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        exclude = ('owner', 'members')
        # fields = ('name', 'description', 'category', 'max_num', 'months')

class EditGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
        }
        exclude = ('owner', 'members')

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class RegistrationForm(UserCreationForm):
    address = forms.CharField(required=True)
    address_two = forms.CharField(required=False)
    city = forms.CharField(required=True)
    state = forms.CharField(required=True)
    zipcode = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'address', 'address_two', 'city', 'state', 'zipcode')