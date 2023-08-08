from django.urls import path
from .views import TodoApiView

urlpatterns = [
    # 클래스로 작성된 뷰 사용시 as_view() 무조건 사용
    path("", TodoApiView.as_view(), name="todo"),
]
