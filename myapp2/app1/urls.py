from django.urls import path
from .views import detail, info

# 앱의 네임스페이스 지정
app_name = "app1"

urlpatterns = [
    path("", detail, name="detail"),
    path("info/", info, name="info"),
]
