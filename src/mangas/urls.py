from django.conf import settings
from django.urls import path

from .import views

urlpatterns = [
    path('', views.home_view, name='home'),
]

if settings.DEBUG: 
    # Debug config for Django
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)