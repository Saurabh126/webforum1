from django.conf.urls import url

from . import views

app_name = 'Login'
urlpatterns  =  [
    url(r'^$', views.loggingin, name='loggingin'),
    url(r'^rr$', views.rr, name='rr'),
    url(r'^addeduser$', views.addeduser, name='addeduser'),
    url(r'^register$', views.register, name='register'),
]
