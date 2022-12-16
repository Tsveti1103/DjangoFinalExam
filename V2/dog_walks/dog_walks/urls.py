from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from dog_walks.exception_handlers import page_not_found_handler, custom_handler500, permission_denied_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dog_walks.common.urls')),
    path('places/', include('dog_walks.places.urls')),
    path('accounts/', include('dog_walks.accounts.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

handler404 = page_not_found_handler
handler500 = custom_handler500
handler403 = permission_denied_handler
