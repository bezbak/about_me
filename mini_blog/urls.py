from django.contrib import admin
from django.urls import path
# from django.conf.urls.static import static
# from django.conf import settings
from me.views import index,second
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index ,name='1'),
    path('second/', second ,name='2'),
]
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)