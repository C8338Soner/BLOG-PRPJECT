from django.urls import path, include
from rest_framework import routers
from .views import PostMVS, CommentMVS, CategoryMVS

router = routers.DefaultRouter()
router.register('postcreate', PostMVS)
router.register('category', CategoryMVS) 
# router.register('comments', CommentMVS) 


urlpatterns = [
    path('', include(router.urls)),
    path('comment/<str:pk>', CommentMVS.as_view()),
    # path('category/', CategoryMVS.as_view()),

]
