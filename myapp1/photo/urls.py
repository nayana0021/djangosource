from django.urls import path
from . import views

urlpatterns = [
    # path(경로,특정 경로에 응답하는 함수,별칭(옵션))
    path("", views.photo_list, name="photo_list"),
    # http://127.0.0.1:8000/photo/1
    path("<int:id>/", views.photo_detail, name="photo_detail"), # 숫자가 들어오면 views 의 photo_detail 함수가 처리할거야 / path 가 스프링의 pathvariable 과 같은 기능
    # http://127.0.0.1:8000/photo/new + get,post
    path("new/", views.photo_post, name="photo_post"),  # 기본으로 /photo/는 잡아준다구~
    # http://127.0.0.1:8000/photo/1/edit
    path("<int:id>/edit/", views.photo_edit, name="photo_edit"),
    # http://127.0.0.1:8000/photo/1/remove
    path("<int:id>/remove/", views.photo_remove, name="photo_remove"),
]
