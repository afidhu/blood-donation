from django.contrib.auth.forms import UserCreationForm
from.models import Users
from django import forms

class userRegisterForm(UserCreationForm):
    class Meta:
        model=Users
        fields=['username', 'email', 'password1', 'password2','is_organization']
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control mt-2", "id":"name"}),
            "email":forms.EmailInput(attrs={"class":"form-control mt-2", "id":"name"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control  mt-2"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control  mt-2"}),
            "is_organization": forms.CheckboxInput(attrs={"class": "form-check-input mt-2"}),
            }
        
    def __init__(self, *args, **kwargs):
        super(userRegisterForm, self).__init__(*args, **kwargs)
        
        # Remove help_text for certain fields
        for fieldname in ('username', 'email', 'password1', 'password2'):
            self.fields[fieldname].help_text = None
        
        # # Add 'form-control' class to all fields
        # for field in self.fields.values():
        #     field.widget.attrs['class'] = 'form-control'
        for fieldname, field in self.fields.items():
            if not isinstance(field.widget, forms.CheckboxInput):  # Skip CheckboxInput
                field.widget.attrs['class'] = 'form-control mt-2'

class LoginForm(forms.Form):
    name=forms.CharField(label="user name / orgonization name", widget=forms.TextInput(attrs={"class":"form-control", "id":"form"}))
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class":"form-control", "id":"form"}))
    