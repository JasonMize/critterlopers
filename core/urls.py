from django.conf.urls import url

from . import views

app_name = 'critterlopers'
urlpatterns = [
    url('', views.IndexView.as_view(), name='index'),
]