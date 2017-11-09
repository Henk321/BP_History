from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.bphistory, name='bphistory'),
    url(r'add/bp/$', views.add_blood_pressure, name='add_bp'),
    url(r'add/weight/$', views.add_weight, name="add_weight"),
]
