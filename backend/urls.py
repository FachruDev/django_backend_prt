from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = (
    [
        path("i18n/", include("django.conf.urls.i18n")),
        path("ckeditor5/", include('django_ckeditor_5.urls')),
    ]
    + i18n_patterns(
        path("admin/", admin.site.urls),
    )
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)