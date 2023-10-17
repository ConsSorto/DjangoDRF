from rest_framework.routers import DefaultRouter
#from post.api.views import PostApiViewSet
from post.api.views import PostModelsViewSet

router_post = DefaultRouter()

#router_post.register(prefix="post", basename='post', viewset=PostApiViewSet)
router_post.register(prefix="post", basename='post', viewset=PostModelsViewSet)

