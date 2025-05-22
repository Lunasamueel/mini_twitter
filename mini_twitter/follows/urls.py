from django.urls import path
from follows.views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('<int:pk>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('<int:pk>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]