from django import forms

class AgeForm(forms.Form):
    my_birth_date = forms.DateField(
        label='生年月日',
        widget=forms.SelectDateWidget(years=range(1900, 2023))
    )
