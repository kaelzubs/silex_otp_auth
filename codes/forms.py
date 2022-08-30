from dataclasses import fields
import email
from django import forms
from . models import Code
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class NewUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('firstname', 'lastname', 'email', 'phone_number', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.firstname = self.cleaned_data['firstname']
        user.lastname = self.cleaned_data['lastname']
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        if commit:
            user.save()
        return user

class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Enter SMS verification code')
    class Meta:
        model = Code
        fields = ('number',)