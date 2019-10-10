from django.conf.urls import url
from botchat.views import ChatterBotAppView, ChatterBotApiView


urlpatterns=[
    url(r'^chaterbot$', ChatterBotAppView.as_view(), name='chat'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),

]