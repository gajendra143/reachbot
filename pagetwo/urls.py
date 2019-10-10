from django.conf.urls import url
from pagetwo import views


urlpatterns=[
    url(r'^$', views.pagetwo, name='main'),
    url(r'^register$', views.Register),
    url(r'^about$', views.about, name='about'),
    url(r'^service$', views.services, name='service'),
    url(r'^regist$', views.rstar, name='register'),
    url(r'^team$', views.team, name='team'),
    url(r'^port$', views.port, name='port'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^login$', views.userLogin, name='login'),
    url(r'^logout$', views.userlogout, name='logout'),
    url(r'^coder$', views.coder, name='coder'),
    url(r'^design$', views.design, name='design'),
    url(r'^wordpress$', views.wordpress, name='wordpress'),
    url(r'^expert$', views.expert, name='expert'),

]