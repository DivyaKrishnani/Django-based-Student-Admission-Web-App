from . import views
from django.conf.urls import url, include

urlpatterns = [
	
    url('$', views.index, name='index'),
]