from django.contrib import admin
from django.urls import path, include
from accounts.views import home
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG == False:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('courses/', include('academy.urls')),
    path('certificate/', include('certificates.urls')),  # ADD THIS  # ADD THIS
]