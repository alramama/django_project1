from blog import views
#from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('', views.home),

]
