from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("",views.IndexView.as_view(),name="main-page"),
    # path("post/<str:title>/",views.SinglePostView,name="single-post"),
    path("post/<slug:pk>/",views.SinglePostView.as_view(),name="single-post"),
    path("author/",views.AuthorView.as_view(),name="all-authors"),
    path("author/<str:author>/",views.SingleAuthorPostView,name="author-post"),
    # path("author/<slug:pk>/",views.SingleAuthorPostView.as_view(),name="author-post"),
    path("posts/",views.AllPostsView.as_view(),name="all-posts"),
    path("posts/recent/",views.RecentPostsView.as_view(),name="recent-posts"),
    path("posts/create/",views.CreateBlogView.as_view(),name="create-post"),
    path("posts/create/thank-you/",views.ThankYouView.as_view(),name="thank-you"),

]
