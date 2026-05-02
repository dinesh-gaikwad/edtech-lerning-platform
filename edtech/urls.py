from django.contrib import admin
from django.urls import path, include
from accounts.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('accounts/', include('allauth.urls')),
    path('courses/', include('academy.urls')),
    path('certificate/', include('certificates.urls')),  # ADD THIS  # ADD THIS
]