from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio.views import homeview
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview, name='homeview')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

