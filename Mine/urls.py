from django.urls import path,include
from .views import BookViewSet, BookDetailViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'bookdetails', BookDetailViewSet, basename="bookdetail")


urlpatterns = [
    path('', include(router.urls)),

]
