from django.urls import path

from .views import ArticleView

app_name = "articles"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]

'''
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='user')

urlpatterns = router.urls
'''
