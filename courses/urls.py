from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('certificate/<int:course_id>/', views.download_certificate, name='download_certificate'),
]