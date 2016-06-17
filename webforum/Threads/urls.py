from django.conf.urls import url

from . import views

app_name = 'Threads'
urlpatterns  =  [
    url(r'^(?P<user_user_username>\w+)$', views.questionspage, name='questionspage'),
    url(r'^(?P<user_user_username>\w+)/(?P<question_id>[0-9]+)/$', views.answerpage, name='answerpage'),
]
