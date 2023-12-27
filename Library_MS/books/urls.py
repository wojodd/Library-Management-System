from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('author', AuthorViewSet, basename='author')
router.register('publisher', PublisherViewSet, basename='publisher')
router.register('language', LanguageViewSet, basename='language')
router.register('category', CategoryViewSet, basename='category')
router.register('section', SectionViewSet, basename='section')
router.register('faculty', FacultyViewSet, basename='faculty')
router.register('book', BookViewSet, basename='book')
router.register('copy', CopyViewSet, basename='copy')
router.register('library', LibraryViewSet, basename='library')
router.register('new', NewViewSet, basename='new')



urlpatterns = [
  path('viewset/', include(router.urls)),
  path('viewset/<int:pk>/', include(router.urls)),


]
