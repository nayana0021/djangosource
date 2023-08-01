from django.urls import path, include
from .views import (
    post_list,
    post_create,
    post_edit,
    post_delete,
    post_detail,
    post_like,
)

app_name = "blog"

urlpatterns = [
    # http://127.0.0.1:8000/blogs/
    path("", post_list, name="post_list"),
    # http://127.0.0.1:8000/blogs/create
    path("create/", post_create, name="post_create"),
    # http://127.0.0.1:8000/blogs/detail/1/
    path("detail/<int:post_id>", post_detail, name="post_detail"),
    # http://127.0.0.1:8000/blogs/edit/1/
    path("edit/<int:post_id>", post_edit, name="post_edit"),
    # http://127.0.0.1:8000/blogs/delete/1/
    path("delete/<int:post_id>", post_delete, name="post_delete"),
    # http://127.0.0.1:8000/blogs/likes/1
    path("likes/<int:post_id>/", post_like, name="post_like"),
]
