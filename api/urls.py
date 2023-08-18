from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'events', views.EventViewSet, basename='events')
# urlpatterns = router.urls

urlpatterns = [
    # path('categories/', views.category_list, name='categories'),
] + router.urls