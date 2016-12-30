from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', (views.AppView.as_view()), name='app'),
]
