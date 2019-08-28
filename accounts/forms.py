from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserModel
import string


class SignupForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ("username", "email", "password")
        labels = {
            'username': _('Choose an identity'),
            'email': _('Email'),
            'password': _('PassPhrase')
        }
        help_texts = {
            'username': _(''),
        }
        error_messages = {
            'username': {
                'max_length': _('identity too long!')
            },
        }
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_password(self):
        password = self.cleaned_data["password"]
        # standard = string.ascii_letters + string.digits \
        #     + string.punctuation

        if len(password) < 6:
            raise forms.ValidationError(
                "Password should have more than 6 characters.")
        # if not set([True if x in standard else False for x in password]):
        #     raise forms.ValidationError("Password must contain an uppercase\
        #         ,lowercase, digit and punctuation")
        uppercase, lowercase, digit, punct, password_passed = \
            False, False, False, False, False
        for character in password:
            if character in string.ascii_uppercase and not uppercase:
                uppercase = True
            if character in string.ascii_uppercase and not lowercase:
                lowercase = True
            if character in string.digits and not digit:
                digit = True
            if character in string.punctuation and not punct:
                punct = True
            if set([uppercase, lowercase, digit, punct]) == {True}:
                password_passed = True
                break
        if not password_passed:
            raise forms.ValidationError(
                "Password must contain an uppercase, lowercase, digit \
                and punctuation")

        return password


class LoginForm(forms.ModelForm):
    """
    Login definition
    """
    class Meta:
        model = UserModel
        fields = ('username', 'password')
    # class
# class SignupForm(forms.Form):
#     """Login definition."""
#     username = forms.CharField(required=True)
#     password = forms.CharField(required=True, widget=forms.PasswordInput())
