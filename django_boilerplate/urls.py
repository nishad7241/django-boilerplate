from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings as SETTINGS
from django.conf.urls.static import static


urlpatterns = [
    path('realestate-admin/', admin.site.urls),

    path('core/', include(('core.urls', 'core'), namespace='core')),

] + static(SETTINGS.STATIC_URL, document_root=SETTINGS.STATIC_ROOT) + static(SETTINGS.MEDIA_URL, document_root=SETTINGS.MEDIA_ROOT)
