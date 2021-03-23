from rest_framework.routers import DefaultRouter

from .views import CommentViewSet


router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='user')

urlpatterns = router.urls

