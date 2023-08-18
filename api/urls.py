from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views
from api.views import CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
# urlpatterns = router.urls

urlpatterns = [
    path('events/', views.event_list, name='events'),
    # path('categories/', views.category_list, name='categories'),
] + router.urls