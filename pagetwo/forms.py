#from django import forms
from pagetwo.models import Register, ebregister
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = '__all__'

        widgets = {
            "name": forms.TextInput(attrs={'placeholder': 'Name'}),
            "mail": forms.TextInput(attrs={'placeholder': 'enter your mail here'}),
            "subject": forms.TextInput(attrs={'placeholder': 'subject'}),
            "message": forms.TextInput(attrs={'placeholder': 'write  your message here'}),
        }

    def __init__(self, *args, **kwargs):
        ''' remove any labels here if desired
        '''
        super(RegisterForm, self).__init__(*args, **kwargs)

        # remove the label of a non-linked/calculated field (txt01 added at top of form)
        self.fields['name'].label = ''

        # you can also remove labels of built-in model properties
        self.fields['mail'].label = ''
        self.fields['subject'].label = ''
        self.fields['message'].label = ''



class userloginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



    # def __init__(self, *args, **kwargs):
    #     super(RegisterForm, self).__init__(*args, **kwargs)
    #     self.fields['description'].widget = TextInput(attrs={
    #         'id': 'myCustomId',
    #         'class': 'myCustomClass',
    #         'name': 'myCustomName',
    #         'placeholder': 'myCustomPlaceholder'})


# class UserForm(forms.ModelForm):
#     password=forms.CharField(widget=forms.PasswordInput())
#     confirm_password=forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = ebregister
#         fields='__all__'
#
#     def clean(self):
#         cleaned_data = super(UserForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError("password and confirm_password does not match")




class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

