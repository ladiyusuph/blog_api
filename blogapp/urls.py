from django.urls import path
from . import views

urlpatterns = [
    path(
        "blogposts/",
        views.BlogPostListCreateView.as_view(),
        name="blogpost-list-create",
    ),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostDetailUpdateView.as_view(),
        name="blogpost-detail",
    ),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostDeleteView.as_view(),
        name="blogpost-delete",
    ),
]
