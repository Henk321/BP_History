from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bphistory, name='bphistory'),
    url(r'post/new/$', views.post_new, name='post_new'),
]
