from binascii import a2b_base64
from django.http import HttpResponse
from django.shortcuts import render

from sys_RegLog.models import  Customer, Owner

# Create your views here.
def hello(request):
    return HttpResponse('Hello world! RegLog')

def sign_up(request):
    return render(request,"sign_up.html")


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import ProfileForm, UserForm, UserRegisterForm, SignupForm, UserResetPwdForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import os

from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token,findback_passwd_token
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str

#from sys_Renter.models import User_Goals
from django.contrib.auth.models import User
from .forms import UserFindPwdEmailForm

from django.forms.models import model_to_dict

  
#################### index#######################################
def index(request):
    current_user = request.user

    return render(request, 'sys_RegLog/index.html', {"userIcon_url:"'title':'HomePage'})
  
########### register here #####################################
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        check_username = request.POST.get('username')
        customer_or_user = request.POST.get('user_type')
        try:
            User = get_user_model()
            check_user = User.objects.get(username=check_username)
        except:
            check_user = None
        if (check_user is not None):
            if check_user.is_active == False:
                check_user.delete()

        if form.is_valid():
            user1 = form.save()
            user1.is_active = False
            current_site = get_current_site(request)
            user1.save()
            if customer_or_user == None:
                customer_or_user = "customer"
            if customer_or_user == "customer":
                user1.profile.user_is_customer = 1
                user1.save()
                Customer.objects.create(user_id = user1.id, name = user1.username, email = user1.email, balance = 500)
            else:
                user1.profile.user_is_customer = 0
                user1.save()
                Owner.objects.create(user_id = user1.id, name = user1.username, email = user1.email)


            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            ######################### mail system ####################################
            htmly = get_template('sys_RegLog/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'zhuhao010801@outlook.com', email
            html_content = htmly.render(d)

            message = render_to_string('sys_RegLog/email_template.html', {
                'user': user1,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user1.pk)),
                'token': account_activation_token.make_token(user1),
                })

            text_content = 'You should click this link to activate your account!'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(message, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'We have sent you an e-mail, please read it to activate your account')
            return redirect('sys_RegLog:login')
    else:
        form = UserRegisterForm()
    return render(request, 'sys_RegLog/register.html', {'form': form, 'title':'Reqister Here'})
  
################ login forms###################################################
def Login(request):
    if request.method == 'POST':
        User = get_user_model()
        # AuthenticationForm_can_also_be_used__
  
        username = request.POST['username']
        password = request.POST['password']
        user1 = authenticate(request, username = username, password = password)

        # If the user log in successfully, then it will go to its profile page, implemented in sys_Renter
        if user1 is not None:
            form = login(request, user1)
            messages.success(request, f' Welcome {username} !!')
            #return redirect('sys_Renter:profile',goal_op=0)
            #user_entry = (User.objects.get(username = username)) # 理论上只有一个User
            #request.session['adminuser'] = user_entry.toDict()
            if user1.profile.user_is_customer == 1:
                return redirect('sys_Purchase:index', showidx=1)
            else:
                return redirect('sys_Renter:goal_index', pIndex=1,status_required = 0)
        else:
            messages.info(request, f'account does not exit plz sign in')
    #form = AuthenticationForm()
    return render(request, 'sys_RegLog/login.html', { 'title':'log in'})



def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

       

        #UserProfile.objects.create(user=user, userIcon_url="UserIcon2/default.jpeg")
        return render(request,"sys_RegLog/successfully_send.html")
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return render(request,"sys_RegLog/successfully_send.html")
        return HttpResponse('Activation link is invalid!')



def forget_pwd(request): # Generate email, including a link to change the pwd
    if request.method == 'POST':

        typed_email = request.POST['email']
        typed_username = request.POST['username']

        try:
            current_user_entry = User.objects.get(username = typed_username, email = typed_email)
            current_user_email = current_user_entry.email
            email = current_user_email
            subject, from_email, to = 'Find Back Your PassWord', 'zhuhao010801@outlook.com', email
            current_site = get_current_site(request)
            message = render_to_string('sys_RegLog/email_template_findpwd.html', {
                'user': current_user_entry,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(current_user_entry.pk)),
                'token': findback_passwd_token.make_token(current_user_entry),
                })
            text_content = 'You should click this link to reset your password!'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(message, "text/html")
            msg.send()
            ##################################################################
            messages.success(request, f'We have sent you an e-mail, please read it to reset your password!')
        except:
            messages.success(request, f'The account does not exist or you input the unmatched email')
            return redirect('sys_RegLog:forget_pwd')


        return redirect('sys_RegLog:login')

        

    form = UserFindPwdEmailForm()

    return render(request, 'sys_RegLog/forget_pwd.html', {'form': form, 'title':'Find back your password'})

    
def redirect_to_resetpwd(request, uidb64, token): # Mainly judge whether the link is correct. If it does, go to the reset pwd page
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user_entry = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user_entry = None
    if user_entry is not None and findback_passwd_token.check_token(user_entry, token):
        form = login(request, user_entry)
        messages.success(request, f' Please reset your passwd {user_entry.username} !!')
        return redirect('sys_RegLog:reset_pwd')      
    else:
        return HttpResponse('Activation link is invalid!')

def reset_pwd(request): # Reset the passwd
    if request.method == 'POST':
        form = UserResetPwdForm(request.POST)
        #form['id'] = request.user.id

        if form.is_valid():
            current_user_id = request.user.id
            new_passwd = form.cleaned_data.get('password1')
            User = get_user_model()
            current_user_entry = User.objects.get(id=current_user_id)
            current_user_entry.set_password(new_passwd)
            current_user_entry.save()
            
            return redirect('sys_RegLog:index')
    else:
        form = UserResetPwdForm()
    return render(request, 'sys_RegLog/reset_passwd.html', {'form': form, 'title':'Reset Pwd'})    




@login_required
def update_profile(request):
    current_user_id = request.user.id
    if request.user.profile.user_is_customer == 1:
        current_customer_owner = Customer.objects.get(user_id = current_user_id)
    else:
        current_customer_owner = Owner.objects.get(user_id = current_user_id)
    #current_customer = Customer.objects.get(user_id = current_user_id)

    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']
        address = request.POST['address']
        email = request.POST['email']

        current_customer_owner.name = name
        current_customer_owner.gender = gender
        current_customer_owner.address = address
        current_customer_owner.email = email

        #current_profile = UserProfile.objects.get(user_id = current_user_id)
        request.user.username = name
        current_customer_owner.save()
        request.user.save()

    
    context = {"customer": current_customer_owner}
    return render(request, 'sys_RegLog/profile2.html', context)
