from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^artwork/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail')
    # url(r'^blog/', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

