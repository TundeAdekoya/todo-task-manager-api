from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import TodoViewSet, UserViewSet 

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', TodoViewSet, basename='tasks')

urlpatterns = router.urls
# urlpatterns = [
#     path('<int:pk>/', TodoDetail.as_view()),
#     path('', TodoList.as_view()),
#     path('users/<int:pk>/', UserDetail.as_view()),
#     path('users/', UserList.as_view()),
# ]
