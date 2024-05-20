from django import forms
from app.models import *
import re


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        help_text ={'username':""}
        widgets = {'password':forms.PasswordInput}

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        exclude =['username']

    def clean_phno(self):
        phno =self.cleaned_data.get["phno"]
        if re.match(r"(?:\+91 ?)?[6-9]\d{9}",phno): 
            return phno
        return None
