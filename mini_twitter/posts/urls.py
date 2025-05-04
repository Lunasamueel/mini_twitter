from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet, ToggleLikeView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:post_id>/like/', ToggleLikeView.as_view(), name='toggle-like')
    
]