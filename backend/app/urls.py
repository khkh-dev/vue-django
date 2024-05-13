from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, RefreshAPIView, NoteViewSet, UserViewSet

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename="notes")
router.register(r'users', UserViewSet, basename="users")

urlpatterns = [
    path('register', RegisterAPIView.as_view(), name="register"),
    path('login', LoginAPIView.as_view(), name="login"),
    path('logout', LogoutAPIView.as_view(), name="logout"),
    path('refresh', RefreshAPIView.as_view(), name="refresh"),
    path('', include(router.urls), name="home"),
]
