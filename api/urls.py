from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "api"
urlpatterns = [
    path('article/', views.get_article, name='get_article'),
    path('article/<article_id>/', views.get_article_filter_by, name='get_details_article'),
    path('user/', views.get_user, name='get_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
