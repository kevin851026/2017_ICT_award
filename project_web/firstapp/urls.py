from django.conf.urls import url, include
from firstapp.views import home,test,update_user,get_art,idlist
from first import settings
urlpatterns = [
    url(r'^home$', home),
    url(r'^test$', test),
    url(r'^update_user$',update_user),
    url(r'^get_art$',get_art),
    url(r'^idlist$',idlist),
]