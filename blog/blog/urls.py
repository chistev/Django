from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from docx import settings

from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', article_views.home, name='home'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
