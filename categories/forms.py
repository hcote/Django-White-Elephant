from django import forms
from .models import Group

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'owner', 'category', 'max_num', 'members', 'months')
