from django.urls import path, include
from .. import user_views, main_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('shop.shop_urls.urls_product_manager')),
    path('', include('shop.shop_urls.urls_user_manager')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
