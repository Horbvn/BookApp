from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('katalog/', include('katalog.urls')),
    path('admin/', admin.site.urls),
]