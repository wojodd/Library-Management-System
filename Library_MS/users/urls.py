from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('semester', SemesterViewSet, basename='Semester')
router.register('cities', CitiesViewSet, basename='cities')
router.register('role', RoleViewSet, basename='role')
router.register('gender', genderViewSet, basename='gender')
router.register('despositves', DespositvesViewSet, basename='despositves')


urlpatterns = [
   path('register/', register_user, name='register'),
   path('login/', user_login, name='login'),
   path('logout/', user_logout, name='logout'),
   path('viewset/', include(router.urls)),
   path('viewset/<int:pk>/', include(router.urls)),
]
