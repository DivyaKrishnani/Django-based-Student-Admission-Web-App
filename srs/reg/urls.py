from . import views
from django.conf.urls import url, include
from django.urls import path

urlpatterns = [
	
    path('', views.index, name='index'),
    #path('homepage2/', views.homepage2, name='homepage2'),
    #path('login-signup/', views.loginsignup, name = 'loginsignup'),
    path('signup/', views.signup, name='signup'),
    path('login/',views.login_view,name="login_view"),

]
