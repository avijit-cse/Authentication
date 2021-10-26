from django import forms
from auth_main.models import  userInfo
from django.contrib.auth.models import User

class userfrom(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields=('username','email','password')


class userInfofrom(forms.ModelForm):
    class Meta():
        model = userInfo
        fields=('fb_id','profile_pic')