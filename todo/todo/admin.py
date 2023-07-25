from django.contrib import admin
from .models import Todo

# admin 페이지에서 관리할 모델 추가
admin.site.register(Todo)
