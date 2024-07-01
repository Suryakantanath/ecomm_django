from django import forms
from newapp.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={
                 'username':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'password':forms.PasswordInput(attrs={'class':'form-control'}),
                 }