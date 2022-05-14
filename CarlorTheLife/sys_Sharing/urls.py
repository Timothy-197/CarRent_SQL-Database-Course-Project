from django.urls import path

from sys_Sharing import views
urlpatterns = [
    path('', views.hello),
]