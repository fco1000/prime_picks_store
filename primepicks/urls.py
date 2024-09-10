from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('apps.account.urls')),
    path('store_admin/',include('apps.administration.urls')),
    path('cart/',include('apps.cart.urls')),
    path('delivery/',include('apps.delivery.urls')),
    path('',include('apps.products.urls')),
    path('vendor/',include('apps.vendor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
