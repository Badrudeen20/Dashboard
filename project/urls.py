from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/',include('crmpanel.urls')),
    # path('admin/', admin.site.urls),
]  
