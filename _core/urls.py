from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([

    ])),
]


if settings.DRF_ENABLED:
    schema_view = get_schema_view(
        openapi.Info(
            title="Pkg Point Admin API",
            default_version='v.1',
        ),
        permission_classes=(permissions.AllowAny,),
        public=settings.DEBUG,
        patterns=urlpatterns,
    )
    schema = schema_view.with_ui('swagger')

    urlpatterns += [
        path('swagger/', schema),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
