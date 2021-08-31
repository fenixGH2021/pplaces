from django.contrib import admin
from django.urls import path, include
from dj_lppp.settings import STATIC_URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizations/', include('organizations.urls')),
    path('', include('pplaces.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)