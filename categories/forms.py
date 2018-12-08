from django import forms
from .models import Group

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'members')
        # fields = ('name', 'description', 'category', 'max_num', 'months')
