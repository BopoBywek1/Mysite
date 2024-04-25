from django import forms
from django.contrib.auth import authenticate

from.models import User

class RegistrationForm(forms.ModelForm):
    Name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    Login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    class Meta:
        model = User
        fields = ('Name', 'Login', 'Password','ID_Roles')
        exclude = ('ID_Roles',)
class LoginForm(forms.Form):
    Login = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    def clean(self):

        Login = self.cleaned_data.get('Login')
        Password = self.cleaned_data.get('Password')
        if Login and Password:
            Login = authenticate(request=self.request, Login=Login, Password=Password)
            if Login is None:
                raise forms.ValidationError('Invalid username or password')
        return super().clean()









