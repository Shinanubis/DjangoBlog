from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "article"
urlpatterns = [
    # ex: /article/
    path('', views.index, name='index'),
    # ex: /article/5/
    path('<article_id>/', views.detail, name='detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
