from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=40, required=True)
    age = forms.IntegerField(max_value=120, min_value=0, required=False)    


    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2','email', 'first_name', 'last_name', 'personal_id', 'age', 'city', 'user_type']
        exclude = ['password', 'user_type']

# class SignUpForm(UserCreationForm):
#     username = forms.CharField(max_length=40, required=True)
#     age = forms.IntegerField(max_value=120, min_value=0, required=False)
#     def __init__(self, include_username=True, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         if not include_username:
#             self.fields.pop('user_type')
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ['username', 'password1', 'password2','email', 'first_name', 'last_name', 'personal_id', 'age', 'city', 'user_type']
#         exclude = ['password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=155)
    password = forms.CharField(max_length=155, widget=forms.PasswordInput)


class CustomUpdateUser(UserChangeForm):
    username = forms.CharField(disabled=True)
    email = forms.EmailField(disabled=True, required=False)
    age = forms.IntegerField(required=False, max_value=120, min_value=0)
    def __init__(self, *args, **kwargs):
        include_user_type = kwargs.pop('include_user_type', True)
        super().__init__(*args, **kwargs)
        if not include_user_type:
            self.fields.pop('user_type')
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username' ,'email', 'first_name', 'last_name', 'personal_id', 'age', 'city', 'user_type']
        exclude = ['password']


class PostCreationForm(forms.ModelForm):
    images = forms.FileField(required=False)
    class Meta:
        model = Post
        fields = '__all__'