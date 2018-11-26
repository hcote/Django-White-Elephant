from django import forms

class NewGroup(ModelForm):
    category = forms.CharField(label='Category')
    max_members = forms.IntegerField(label='Number of Members')
    start_date = forms.DateField(label='Start Date')
    months = forms.IntegerField(label='Number of Months')
