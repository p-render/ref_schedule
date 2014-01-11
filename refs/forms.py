from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from refs.models import Ref

class RegistrationForm(ModelForm):
    username        = forms.CharField(label=(u'User Name'))
    first_name      = forms.CharField(label=(u'First Name'))
    last_name       = forms.CharField(label=(u'Last Name'))
    email           = forms.EmailField(label=(u'Email Address'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
    password1       = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = Ref
        exclude = ('user', 'first_name', 'last_name')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
                User.objects.get(username=username)
        except User.DoesNotExist:
                return username
        raise forms.ValidationError("That name is already taken, please try another.")

class LoginForm(forms.Form):
    username        = forms.CharField(label=(u'User Name'))
    password        = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
                		