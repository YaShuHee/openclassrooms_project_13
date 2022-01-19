from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .settings import DEBUG
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include("lettings.urls", namespace="lettings")),
    path('profiles/', include("profiles.urls", namespace="profiles")),
    path('admin/', admin.site.urls),
]

if DEBUG:
    # staticfiles won't be served by wsgi (not a web server), so we provide the urls
    urlpatterns += staticfiles_urlpatterns()
