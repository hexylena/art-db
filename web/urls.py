from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^artwork/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
    # url(r'^blog/', include('blog.urls')),
]
