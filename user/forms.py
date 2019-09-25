from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Profile, User, UserImage
import string
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    phone = forms.CharField(max_length=11, required=True)

    class Meta:
        model = User
        fields = ('username', "email", "password")
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'password': "PassPhrase",
        }
        help_texts = {
            "username": _(""),
        }

    def clean_password(self):
        password = self.cleaned_data["password"]
        # standard = string.ascii_letters + string.digits \
        #     + string.punctuation

        if len(password) < 6:
            raise forms.ValidationError(
                "Password should have more than 6 characters.")
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

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username__iexact=username).exists():
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


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'location', 'phone')


class ImageForm(forms.ModelForm):
    # user = forms.ModelChoiceField(
    #     widget=forms.HiddenInput,
    #     queryset=get_user_model().objects.all(),
    #     disabled=True
    # )

    # profile = forms.ModelChoiceField(
    #     widget=forms.HiddenInput,
    #     queryset=get_user_model().objects.filter(),
    #     disabled=True
    # )

    # profile, user = None, None
    class Meta:
        model = UserImage
        fields = ('image',)

    def save(self, *args, **kwargs):
        _image = UserImage.objects.create(
            user=kwargs['user'], profile=kwargs['profile'], image=kwargs['image'])
        _image.save()
