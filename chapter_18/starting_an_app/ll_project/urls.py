# 知识点：配置项目 URL，将请求分发到 learning_logs 应用。

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("learning_logs.urls")),
]
