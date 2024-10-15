from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('propiedades', views.propiedades, name='propiedades'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

