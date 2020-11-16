from . import views
from django.urls import path




urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('',views.index),
    # post.video.url
    # path('',views.index),
]

