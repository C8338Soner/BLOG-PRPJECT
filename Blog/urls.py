from django.urls import path, include
from rest_framework import routers
from .views import PostMVS, CommentMVS, CategoryMVS

router = routers.DefaultRouter()
router.register('postcreate', PostMVS)
router.register('category', CategoryMVS) 


urlpatterns = [
    path('', include(router.urls)),
    path('comment/', CommentMVS.as_view()),
    # path('category/', CategoryMVS.as_view()),

]
