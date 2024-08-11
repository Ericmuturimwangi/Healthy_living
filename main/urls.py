from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("djrichtextfield/", include("djrichtextfield.urls")),
    path("", include("home.urls")),
    path("recipes/", include("recipes.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
