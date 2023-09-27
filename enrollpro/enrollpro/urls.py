"""
URL configuration for enrollpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from enrollapp import views
from django.conf.urls.static import static
from django.conf import  settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('login',views.Login,name="login"),
    path('signup/',views.Signup,name="signup"),
    path('trainer/',views.Trainers,name="trainer"),
    path('logout/',views.logout,name="logout"),
    path('details/<rid>',views.Detail,name="details"),
    path('search/',views.searching,name="search"),
    path('filprice/<x>',views.filters,name="filprice"),
    path('payment/<rid>',views.payments,name="payment"),
    path('order',views.generate_order,name="order"),
    #path('Done',views.done,name='Done'),
    path('email',views.Email,name='email'),
    #path('success',views.Success,name='success'),
    #path('payment',views.email,name='payment'),
    #path('ordersuccess/',views.order_complete,name="success"),
]



if settings.DEBUG:
    
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
