from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import include, path
from afrc.views.settings_api import SettingsAPI
from afrc.views.map_api import MapDataAPI, FeatureBufferAPI, GeoJSONBoundsAPI

urlpatterns = [
    # project-level urls
    path("api-settings", SettingsAPI.as_view(), name="api-settings"),
    path("api-map-data", MapDataAPI.as_view(), name="api-map-data"),
    path("api-feature-buffer", FeatureBufferAPI.as_view(), name="api-feature-buffer"),
    path("api-geojson-bounds", GeoJSONBoundsAPI.as_view(), name="api-geojson-bounds"),
]

# Ensure Arches core urls are superseded by project-level urls
urlpatterns.append(path("", include("arches.urls")))

# Adds URL pattern to serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Only handle i18n routing in active project. This will still handle the routes provided by Arches core and Arches applications,
# but handling i18n routes in multiple places causes application errors.
if settings.ROOT_URLCONF == __name__:
    if settings.SHOW_LANGUAGE_SWITCH is True:
        urlpatterns = i18n_patterns(*urlpatterns)

    urlpatterns.append(path("i18n/", include("django.conf.urls.i18n")))
