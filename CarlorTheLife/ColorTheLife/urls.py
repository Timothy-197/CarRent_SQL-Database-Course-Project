"""ColorTheLife URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings



from django.contrib import admin
from django.urls import path, include
from sys_RegLog import views as user_view
from django.contrib.auth import views as auth
from django.conf.urls.static import static

urlpatterns = [
    #path('', include(('sys_RegLog.urls'))),
    path('admin/', admin.site.urls),

    # 5 systems
    #path('reglog/', include("sys_RegLog.urls")),
    #path('clockin/', include("sys_ClockIn.urls")),
    #path('colortile/', include("sys_ColorTile.urls")),
    #path('purchase/', include("sys_Purchase.urls")),
    #path('sharing/', include("sys_Sharing.urls")),


    path('reglog/', include(('sys_RegLog.urls','sys_RegLog'),namespace="sys_RegLog")),
    #path('clockin/', include(('sys_ClockIn.urls','sys_ClockIn'),namespace="sys_ClockIn")),
    path('clockin/', include(('sys_ClockIn.urls','sys_ClockIn'),namespace="sys_ClockIn")),
    path('purchase/', include(('sys_Purchase.urls','sys_Purchase'),namespace="sys_Purchase")),
    path('colortile/', include(('sys_ColorTile.urls','sys_ColorTile'),namespace="sys_ColorTile"))
]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
