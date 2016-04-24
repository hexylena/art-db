from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^artwork/(?P<pk>[0-9]+)/$', views.ArtworkUpdate.as_view(), name='artwork-update'),
    url(r'^account/', include('account.urls')),
    url(r'^$', views.home, name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


