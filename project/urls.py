from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls import handler404,handler500
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import serve

def custom_404(request, exception):
    return render(request, '404.html', status=404)

handler404 = custom_404

urlpatterns = [
    path('',include('crmpanel.urls')),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    # path('admin/', admin.site.urls),
]  

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


