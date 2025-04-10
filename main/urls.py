from django.conf.urls.static import static
from django.urls import path

from sitetablica import settings
from . import views
urlpatterns = [
    path('', views.index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)