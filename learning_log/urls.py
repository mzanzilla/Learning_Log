
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path


app_name = "learning_logs"
urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r'', learning_log.urls),
    path(r'', include('learning_logs.urls')),
]
