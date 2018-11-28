from django import forms
from .models import Group

class NewGroup(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('category', 'members', 'start_date', 'months')
