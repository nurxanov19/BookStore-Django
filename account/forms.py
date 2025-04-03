from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class UserForm(forms.ModelForm):
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())
    confirm_password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username',  'email', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError('Password and Confirm Password should be same')

        return cleaned_data

    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data['password'])  # Hashes the password
    #     if commit:
    #         user.save()
    #     return user