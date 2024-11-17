from django.conf.urls.static import static
from django.conf import settings

from django.urls import path
from work import views

app_name = 'work'
urlpatterns = [
    path('', views.home, name="home"),
    path('enquiry/', views.enquiry, name="enquiry"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)