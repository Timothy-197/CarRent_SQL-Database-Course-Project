
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from sys_RegLog.models import UserProfile
#from sys_ClockIn.models import User_Goals
 
from django import forms
from django.core.files.images import get_image_dimensions

 
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #phone_no = forms.CharField(max_length = 20)
    #first_name = forms.CharField(max_length = 20)
    #last_name = forms.CharField(max_length = 20)
    #LiYUXiaosb = forms.CharField(max_length = 20)
    class Meta:
        model = User
        #fields = ['username', 'email', 'phone_no', 'password1', 'password2','first_name','last_name']
        fields = ('username', 'email', 'password1', 'password2')

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserFindPwdEmailForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['id','username','email']

class UserResetPwdForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['id','password1', 'password2']   

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('userIcon_url','userIntro', 'userJob', 'userHobby', 'userMobile','userLocation','user_is_customer')
