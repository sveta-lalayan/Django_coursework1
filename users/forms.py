# from django.contrib.auth.forms import UserCreationForm
# from django.forms import forms, EmailField
#
# from mailing.forms import StyleFormMixin
# from users.models import User
#
#
# class UserRegisterForm(StyleFormMixin, UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("email", "password1", "password2")
#
#
# class PasswordResetForm(forms.Form):
#     email = EmailField(label="Email", max_length=254)


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import EmailField

from mailing.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "password1", "password2")


class PasswordResetForm(forms.Form):
    email = EmailField(label="Email", max_length=254)


class UserProfileForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'country', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = False