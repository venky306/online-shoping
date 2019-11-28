"""pro1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='show.html')),
    path('home/',views.home,name='home'),
    # merchant
    path('mlogin/',views.mlogin,name='mlogin'),
    path('mregister/',views.mregister,name='mregister'),
    path('esavereg/',views.esavereg,name='esavereg'),
    path('viewmr/',views.viewmr,name='viewmr'),
    path('adhome/',views.adhome,name='adhome'),
    path('delmt/',views.delmt,name='delmt'),
    path('deletemerch/',views.deleteMerchant,name='deletemerch'),
    path('logout/',views.logout,name='logout'),
    # other django application of merchent login checking page
    path('merchentpagelogin/<str:email>&<str:password>/',views.Merchentpagelogin.as_view()),
    # change password using other django application (merchant application)
    path('change/<str:email>&<str:password>/',views.Change.as_view()),
#     product saving request sending
    path('saveproduct/',views.Productsave.as_view(),name='saveproduct')
]
