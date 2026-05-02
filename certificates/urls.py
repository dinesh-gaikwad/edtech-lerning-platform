from django.urls import path
from .views import generate_certificate

app_name = 'certificates'
urlpatterns = [
    path('generate/<int:course_id>/', generate_certificate, name='generate'),
]