"""jobportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from appp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('addjob/',Addjob,name='addjob'),
    path('crlogo/<int:pid>',Crlogo,name='crlogo'),
    path('culogo/<int:pid>',Culogo,name='culogo'),
    path('joblist/',Joblist,name='joblist'),
    path('sjl/',Sjl,name='sjl'),
    path('sjoblist/',SJoblist,name='sjoblist'),
    path('description/<int:pid>',Description,name='description'),
    path('editjobdetail/<int:pid>',Editjobdetail,name='editjobdetail'),
    path('adminlogin/',Adminlogin,name='adminlogin'),
    path('adminhome/',Adminhome,name='adminhome'),
    path('cpadmin/',Cpadmin,name='cpadmin'),
    path('userlogin/',Userlogin,name='userlogin'),
    path('cpuser/',Cpuser,name='cpuser'),
    path('cprecruiter/',Cprecruiter,name='cprecruiter'),
    path('recruiterlogin/',Recruiterlogin,name='recruiterlogin'),
    path('recruiterhome/',Recruiterhome,name='recruiterhome'),
    path('recruiterpending/',Recruiterpending,name='recruiterpending'),
    path('recruiteraccepted/',Recruiteraccepted,name='recruiteraccepted'),
    path('recruiterrejected/',Recruiterrejected,name='recruiterrejected'),
    path('allrecruiter/',Allrecruiter,name='allrecruiter'),
    path('deleterecruiter/<int:pid>',Deleterecruiter,name='deleterecruiter'),
    path('deletejob/<int:pid>',Deletejob,name='deletejob'),
    path('changestatus/<int:rid>/',Changestatus,name='changestatus'),
    path('changelogo/<int:rid>/',Changelogo,name='changelogo'),
    path('signup/',Signup,name='signup'),
    path('userhome/',Userhome,name='userhome'),
    path('Logout/',Logout,name='Logout'),
    path('viewuser/',Viewuser,name='viewuser'),
    path('deleteuser/<int:sid>',Deleteuser,name='deleteuser'),
    path('recsignup/',Recsignup,name='recsignup')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
