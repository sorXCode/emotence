from django import forms
from django.utils.translation import gettext_lazy as _
from .models import UserModel
import string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

class SignupForm(forms.ModelForm):
    password = forms.CharField(min_length=6,
                               strip=False,
                               label=_('PassPhrase'),
                               widget=forms.PasswordInput,
                               )

    class Meta:
        model = UserModel
        fields = ("raw_username", "email")
        labels = {
            'raw_username': _('Choose an identity'),
            'email': _('Email'),
        }
        help_texts = {
            'raw_username': _(''),
        }
        error_messages = {
            'raw_username': {
                'max_length': _('identity too long!'),
                'exists': _('Try again, Username Taken')
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


    def clean_raw_username(self):
        username = self.cleaned_data['raw_username']
        if get_user_model().objects.filter(username=username.lower()).exists():
            raise forms.ValidationError(
                "Username Taken, Try another.."
            )
        return username

class LoginForm(AuthenticationForm):
    """
    Login definition
    """

    def clean_username(self):
        return self.cleaned_data['username'].lower()