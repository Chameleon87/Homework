from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from models import Member
from django.contrib.auth.forms import UserCreationForm

class CreateMember(ModelForm):
    username        = forms.CharField(label=(u'User Name'))
    email           = forms.EmailField(label=(u'Email Address'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
    
    class Meta:
        model = Member
        exclude = ('user',)
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
                return username
        raise forms.ValidationError("That Username is already taken!")
        
    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError("Passwords do not match!")
        return self.cleaned_data
        
class LoginForm(forms.Form):
        username = forms.CharField(label=(u'User Name'))
        password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
