from django.urls import path
#from ColorTheLife.sys_RegLog.views import reset_passwd
#from sys_RegLog.views import forget_pwd

from sys_RegLog import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from sys_RegLog import views as user_view
from django.contrib.auth import views as auth


urlpatterns = [
    #path('', views.hello),
    path('', views.index, name ='index'),
    path('login/', user_view.Login, name ='login'),
    path('logout/', auth.LogoutView.as_view(template_name ='sys_RegLog/index.html'), name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('activate/<slug:uidb64>/<slug:token>/', user_view.activate, name ='activate'),
    path('forget_pwd/',user_view.forget_pwd,name="forget_pwd"),
    path('redirect_to_resetpwd/<slug:uidb64>/<slug:token>/', user_view.redirect_to_resetpwd,name="redirect_to_resetpwd"),
    path('reset_pwd/',user_view.reset_pwd,name="reset_pwd"),
    path('changeprofile/', user_view.update_profile, name="update_profile")
]

app_name = "sys_RegLog"