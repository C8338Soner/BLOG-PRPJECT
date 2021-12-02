from django.urls import path, include
from rest_framework import routers
from .views import PostMVS, CommentMVS

router = routers.DefaultRouter()
router.register('postcreate', PostMVS)
# router.register('comment', CommentMVS)


urlpatterns = [
    path('', include(router.urls)),
    path('comment/', CommentMVS.as_view()),

]
