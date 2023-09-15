

from django.conf.urls.static import static
from django.contrib.sites.models import Site

from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("auth/", include("apps.user.urls")),
    path('admin/', admin.site.urls),
]
