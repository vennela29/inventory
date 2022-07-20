"""inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app_ims.views import HomeView,InsertInput,InserView,DisplayView,DeleteInputView,DeleteView,UpdateInputView,UpdateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_ims/',HomeView.as_view()),
    path('app_ims/insertinput/',InsertInput.as_view()),
    path('app_ims/insertinput/insert/',InserView.as_view()),
    path('app_ims/display/',DisplayView.as_view()),
    path('app_ims/deleteinput/',DeleteInputView.as_view()),
    path('app_ims/deleteinput/delete/',DeleteView.as_view()),
    path('app_ims/updateinput/',UpdateInputView.as_view()),
    path('app_ims/updateinput/update/',UpdateView.as_view()),
    path('logout/', logoutPage, name='logout'),
    path('adminpage/',Adminpage,name='adminpage'),
    path('aboutus/', Aboutus, name='aboutus'),
    path('contactus/', Contactus, name='contactus'),
    path('login/', loginPage, name='login'),
    path('register/', registerPage, name='register'),
]
