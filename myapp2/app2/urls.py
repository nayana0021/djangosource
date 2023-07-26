from django.urls import path
from .views import index

app_name = "app2"


urlpatterns = [
    path("", index, name="detail"),
]
