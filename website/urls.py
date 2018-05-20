from django.conf.urls import url

from . import views

app_name = 'website'

urlpatterns = [
    url(r'^$', views.main, name='main'),
]